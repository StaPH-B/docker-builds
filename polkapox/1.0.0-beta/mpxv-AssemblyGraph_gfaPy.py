#!/usr/bin/env python3

### Written by S.Morrison and K. Knipe
### Date: 20221018

import gzip, argparse,os,sys,fnmatch,subprocess,re
import os.path
from datetime import datetime
import linecache
import gfapy
import networkx as nx
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import functools
import operator
from Bio import SeqIO
import pprint
import json

def readGFA(gfa):
	### Read GFA file into gfapy python structure
	try:
		gfaGraph = gfapy.Gfa.from_file(gfa)
		check = "PASS"
		if(len(gfaGraph.edges)) ==0:
			check = "WARNING: gfa file only contains segment lines"
			gfaGraph = "WARNING: gfa file only contains segment lines"
	except:
		check = "WARNING: Issue with GFA file : No GFA processing"
		gfaGraph = "WARNING: Issue with GFA file : No GFA processing"
	return gfaGraph,check


def remove_loops(lnkInfo):
	### Identify contigs with self hits, remove those links
	selfHits = []
	prunedSelfs = []
	for i in lnkInfo:
		if i.from_name == i.to_name:
			selfHits.append(i)

	for j in lnkInfo:
		if not j in selfHits:
			prunedSelfs.append(j)

	check = "PASS"
	return prunedSelfs,check

def id_low_cov_contigs(segInfo):
	### Identify contigs below 0.5x coverage
	lowCov = []
	for i in segInfo:
		line = i.tagnames
		for j in line:
			if j == 'dp':
				if i.get(j) < 0.5:
					name = i.get('name')
					lowCov.append(name)
	check= "PASS"
	return lowCov,check

def remove_low_cov_contigs_from_edges(lowCov,selfHits):
	### Remove low coverage hits from links (after self hits)
	fLinks = []
	
	if len(lowCov) ==0:
		fLinks = selfHits
		check = "PASS"
	elif len(lowCov) ==1:
		for m in lowCov:
			lowID = m
			for n in range(0,len(selfHits)):
				if not((lowID == selfHits[n].from_name) or (lowID == selfHits[n].to_name)):
					fLinks.append(selfHits[n])
		check="PASS"
	else:
		check="[Warning :: There are 2 or more contigs with coverage less than 0.5 - manual review required]"
	return fLinks,check

def find_longest_contig(seqs, gfa):
	### Find the longest contig sequence and its name
	lgContig ={}
	
	for j in seqs:
		leng = j.tagnames
		name = j.get('name')
		for m in leng:
			if m == 'LN':
				seqLen = j.get(m)
				lgContig[name]=seqLen
	lgSeq = max(lgContig,key=lgContig.get)
	
	
	#write longest contig to file
	for j in seqs:
		if lgSeq == j.get('name'):
			SeqIO.write(SeqRecord(Seq(j.get('sequence')),lgSeq), gfa + "_longest.fasta", "fasta")

	#write all contigs to a file
			gfaContigs = open(gfa + "_all_contigs.fasta", "w")
	for n in seqs:
		seqName = n.get('name')
		gfaContigs.write(">"+seqName+"\n")
		gfaContigs.write(n.get('sequence')+"\n")
	gfaContigs.close()		
	check="PASS"
	return lgSeq,check	

def create_filtered_graph(lnks):
	### Create NetworkX Graph
	tGraph = nx.MultiGraph()
	edgeCorrect =[]
	for m in lnks:
		tGraph.add_edge(m.from_name,m.to_name)
	check="PASS"
	if not nx.is_connected(tGraph):
		check="WARNING :: This assembly graph does not appear to be connected -- there may be an assembly issue!"
	else:
		check = "PASS"
	return tGraph,check
	
def get_final_path( graph, longest_contig ):
	### This is the function to assess if there are multiple paths
	### duplicate pairs of contig links with different orientations
	contigs = []
	all_simple_paths = {}
	lengths = {}
	longest_path = []
	final_path = []
	### Check to see if longest contig in edge list to connect contig seqs, dups not removed
	edgeList = list(graph.edges)
	edgeCheck =[]
	for i in edgeList:
		edgeCheck.append(i[2])
	goEdge = list(set(edgeCheck))
	if not len(goEdge) == 1:
		status = "WARNING: Multiple links connect to 2 or more contigs in assembly"
		return final_path, status
	else:
		out = [item for t in edgeList for item in t]

		if not longest_contig in out:
			status = "WARNING: Longest contig not in links to connect to other contigs in assembly "
			return final_path, status

		for edge in graph.edges:
			if edge[0] not in contigs:
				contigs.append(edge[0]) 
			if edge[1] not in contigs:
				contigs.append(edge[1]) 
		for contig in contigs:
			if contig != longest_contig:
				for sp in nx.all_simple_paths( graph, longest_contig, contig ):
					if contig not in all_simple_paths:
						all_simple_paths[contig] = []
					all_simple_paths[contig].append( sp )
					if len(sp) > len(longest_path):
						longest_path = sp
					if len(sp) not in lengths:
						lengths[len(sp)] = 0
					lengths[len(sp)] = lengths[len(sp)] + 1
	####REVERSE THE ITR length path instead of the first path of the all paths section######	
	#warning if there is more than one longest path
		if lengths[len(longest_path)] > 1:
			status = "WARNING: >1 longest path"
			return final_path, status
	
	# make sure there are 2 paths between the longest contig and the last contig in the longest path
		sp_l = all_simple_paths[longest_path[-1]]
		if len(sp_l) < 2:
			status = "WARNING: only 1 path between longest contig and the last contig in the longest path"
			return final_path, status
		elif len(sp_l) == 2:


			path_a = sp_l[0]
			path_b = sp_l[1]

			if len(path_a) < len(path_b):
				path_a.reverse()
				final_path = path_a + path_b[1:]
			elif len(path_b) < len(path_a):
				path_b.reverse()
				final_path = path_b + path_a[1:]


			status = "PASS"
			return final_path, status
		elif len(sp_l) > 2:
			status = "WARNING: >2 paths between longest contig and the last contig in the longest path"
			return final_path, status


def orient_longest_contig(query,reference):
	blastResults = query+"_blast.out"
	subprocess.call(["makeblastdb","-in",query,"-out",query+"_DB","-dbtype","nucl"],shell=False)
	subprocess.call(["blastn","-query", reference,"-db", query+"_DB","-evalue",".00001","-outfmt","6 qseqid sseqid pident length qcovs sstart send sseq mismatch gapopen qlen slen bitscore","-out",blastResults])
	check = "PASS"
	with open(blastResults,'r') as e:
		for line in e:
			f13LInfo = line.split('\t')
			sstart = int(f13LInfo[5])
			send = int(f13LInfo[6])
	orientation = 1 if sstart < send else int(-1)
	
	#TODO - cleanup blast files

	return orientation, check



def get_final_orientation(final_path, lnks, longest_contig, longest_orient):
	contig_orientation = [0] * len(final_path)

	for i in range(final_path.index(longest_contig), len(final_path)):
		if i == final_path.index(longest_contig):
			contig_orientation[i] = longest_orient
		else:
			flag=0
			for link in lnks:
				if (link.from_name == final_path[i-1] and link.to_name == final_path[i]):
					from_orient = 1 if link.from_orient == '+' else int(-1)
					to_orient = 1 if link.to_orient == '+' else int(-1)
					contig_orientation[i] = contig_orientation[i-1] * from_orient * to_orient
					flag=1
			if flag == 0:
				for link in lnks:
					if (link.to_name == final_path[i-1] and link.from_name == final_path[i]):
						from_orient = 1 if link.from_orient == '+' else int(-1)
						to_orient = 1 if link.to_orient == '+' else int(-1)
						contig_orientation[i] = contig_orientation[i-1] * from_orient * to_orient
						flag=1

	for i in range(final_path.index(longest_contig)-1, -1 ,-1):
		flag=0
		for link in lnks:
			if (link.to_name == final_path[i+1] and link.from_name == final_path[i]):
				from_orient = 1 if link.from_orient == '+' else int(-1)
				to_orient = 1 if link.to_orient == '+' else int(-1)
				contig_orientation[i] = contig_orientation[i+1] * from_orient * to_orient
				flag=1
		if flag == 0:
			for link in lnks:
				if (link.from_name == final_path[i+1] and link.to_name == final_path[i]):
					from_orient = 1 if link.from_orient == '+' else int(-1)
					to_orient = 1 if link.to_orient == '+' else int(-1)
					contig_orientation[i] = contig_orientation[i+1] * from_orient * to_orient
					flag=1
		check="PASS"
	return contig_orientation, check

def get_final_sequence(contig_order, contig_orientation, segments):
	segment_info = {}
	for segment in segments:
		segment_count = contig_order.count(segment.get('name'))
		coverage = float(segment.get('dp')) if segment_count == 0 else float(segment.get('dp'))/contig_order.count(segment.get('name'))
		segment_info[segment.get('name')] = {   'coverage' : coverage,
												'sequence' : Seq(segment.get('sequence')),
												'sequence_rc' : Seq(segment.get('sequence')).reverse_complement()
											}
	final_sequence = ''
	final_order_orientation_copy_number = []
	for i in range(len(contig_order)):
		sequence = segment_info[contig_order[i]]['sequence'] * round(segment_info[contig_order[i]]['coverage'])
		if contig_orientation[i] == -1:
			sequence = segment_info[contig_order[i]]['sequence_rc'] * round(segment_info[contig_order[i]]['coverage'])
		orientation = '+' if contig_orientation[i] == 1 else '-'
		order_orientation_copy_number = '%s%s' % (orientation, contig_order[i])
		if round(segment_info[contig_order[i]]['coverage']) > 1:
			order_orientation_copy_number = '%sx%s' % (order_orientation_copy_number, round(segment_info[contig_order[i]]['coverage']))
		final_sequence = final_sequence + sequence
		final_order_orientation_copy_number.append(order_orientation_copy_number)
	
	check = "PASS"
	# are all segments in final_sequence?
	for segment in segment_info:
		if (segment_info[segment]['coverage'] > 0.5) and (segment not in contig_order):
			check = 'WARNING: missing segments'
	return final_sequence, len(final_sequence), " ".join(final_order_orientation_copy_number), check

def get_itr_length(lgContig,contig_order,segments):
	final_itr_length = 0
	itr=[]
	for i in contig_order:
		if not i == lgContig:
			itr.append(i)
		elif i == lgContig:
			break
	for segment in segments:
		segmentName = segment.get('name')
		segmentCov = segment.get('coverage')
		if segmentName in itr:
			segment_coverage = segment.get('dp')
			half_coverage = segment_coverage /2
			segment_sequence_length = len(segment.get('sequence'))
			total_itr_segment_length = segment_sequence_length * round(half_coverage)
			final_itr_length = final_itr_length + total_itr_segment_length
	check = "PASS"
	return final_itr_length , check

def write_log_and_exit( log, status ):

	log_file = os.path.join(log['00']['input']['output_dir'], log['00']['input']['sample_name'] + ".log")
	summary_file = os.path.join(log['00']['input']['output_dir'], log['00']['input']['sample_name'] + ".summary")

	headers = ['sample', 'status', 'contig_order', 'contig_orientation', 'contig_order_orientation_copy_number', 'assembly_length', 'itr_length']
	data = []
	if '00' in log:
		data.append( log['00']['input']['sample_name'] )
		data.append( status )
	if '06' in log:
		data.append( ",".join( str(i) for i in log['06']['output']['final_path']) )
	if '08' in log:
		data.append( ",".join( str(i) for i in log['08']['output']['final_orientation'] ) )
	if '09' in log:
		data.append( str(log['09']['output']['final_order_orientation_copy_number']) )
		data.append( str(log['09']['output']['final_sequence_length']) )
	if '10' in log:
		data.append( str(log['10']['output']['final_itr_length']))

	with open(summary_file, 'w') as f:
		f.write( '\t'.join( headers ) + '\n' )
		f.write( '\t'.join(data) + '\n' )
		
	with open(log_file, 'w') as f:
		json_object = json.dumps(log, indent = 4) 
		f.write(json_object)
	
def main(arguments):
	parser = argparse.ArgumentParser(description="GFA parser to construct assembly from Unicycler", epilog="______")
	parser.add_argument('-i',type=str,required=True,help="GFA file from Unicycler")
	parser.add_argument('-r',type=str,required=True,help="Monkeypox genome sequence - single line fasta")
	parser.add_argument('-o',type=str,required=True,help="Output directory")

	args = parser.parse_args()
	gfaFile = args.i
	refSeq = args.r
	out_dir = args.o
	
	log = {}
	errors = []
	logFile = []
	logFile.append(gfaFile)

	# read gfa file into graph structure
	original_graph, status = readGFA(gfaFile)
	log['00'] = {'step_name'			: "read_gfa",
				'step_description'	: "read gfa file into graph structure",
				'status'			: status,
				'input'				: {
					'gfa'			: gfaFile,
					'sample_name'	: os.path.splitext(os.path.basename(gfaFile))[0],
					'output_dir'	: out_dir
					},
				'output'			: {
					'original_graph'	: str(original_graph),
					}
				}
	if status != "PASS":
		write_log_and_exit(log, status)
	
	# filter edges that are loops (these represent repeats, we'll deal with them later)
	if type(original_graph) == str:
		
		sys.exit(0)
	else:
		filtered_edges, status = remove_loops( original_graph.edges )
		log['01'] = {'step_name'			: "remove_loops",
				'step_description'	: "filter edges that are loops (these represent repeats, we'll deal with them later)",
				'status'			: status,
				'output'			: {
					'filtered_edges'	: str(filtered_edges)
					}
				}
		if status != "PASS":
			write_log_and_exit(log, status)
	
	# identify low coverage contigs
		low_cov_contigs, status = id_low_cov_contigs( original_graph.segments )
		log['02'] = {'step_name'			: "id_low_cov_contigs",
				'step_description'	: "identify low coverage contigs",
				'status'			: status,
				'output'			: {
					'low_cov_contigs'	: low_cov_contigs
					}
				}
		if status != "PASS":
			write_log_and_exit(log, status)
	
	# remove low coverage contigs from edges
	filtered_edges, status = remove_low_cov_contigs_from_edges( low_cov_contigs, filtered_edges )
	log['03'] = {'step_name'			: "remove_low_cov_contigs_from_edges",
				'step_description'	: "remove low coverage contigs from edges",
				'status'			: status,
				'output'			: {
					'filtered_edges'	: str(filtered_edges)
					}
				}
	if status != "PASS":
		write_log_and_exit(log, status)
		sys.exit(0)
	
	# find the longest contig
	longest_contig, status = find_longest_contig( original_graph.segments, log['00']['input']['sample_name'] )
	log['04'] = {'step_name'			: "find_longest_contig",
				'step_description'	: "find the longest contig",
				'status'			: status,
				'output'			: {
					'longest_contig'	: longest_contig
					}
				}
	if status != "PASS":
		write_log_and_exit(log, status)
	
	# create graph from filtered edges
	filtered_graph, status = create_filtered_graph(filtered_edges)	
	log['05'] = {'step_name'			: "create_filtered_graph",
				'step_description'	: "create graph from filtered edges",
				'status'			: status,
				'output'			: {
					'filtered_graph'	: str(filtered_graph)
					}
				}
	if status != "PASS":
		write_log_and_exit(log)
		sys.exit(0)
	
	final_path, status = get_final_path( filtered_graph, longest_contig )
	log['06'] = {'step_name'			: "get_final_path",
				'step_description'	: "get final path from filtered graph using longest contig to longest simple path",
				'status'			: status,
				'output'			: {
					'final_path'	: final_path
					}
				}	
	if status != "PASS":
		write_log_and_exit(log, status)
		sys.exit(0)

	# orient longest contig with F13L
	longest_orientation, status = orient_longest_contig( log['00']['input']['sample_name'] + "_longest.fasta" , refSeq )
	log['07'] = {'step_name'			: "orient_longest_contig",
				'step_description'	: "get orientation of longest contig given F13L gene",
				'status'			: status,
				'output'			: {
					'longest_orientation'	: longest_orientation
					}
				}
	if status != "PASS":
		write_log_and_exit(log)
	
	final_orientation, status = get_final_orientation(final_path, filtered_edges, longest_contig, longest_orientation)
	log['08'] = {'step_name'			: "get_final_orientation",
				'step_description'	: "get orientation of contigs starting at the longest and traversing the path in either direction",
				'status'			: status,
				'output'			: {
					'final_orientation'	: final_orientation
					}
				}	
	if status != "PASS":
		write_log_and_exit(log, status)
	
	final_sequence, final_sequence_length, final_order_orientation_copy_number, status = get_final_sequence( final_path , final_orientation , original_graph.segments )
	log['09'] = {'step_name'			: "get_final_sequence",
				'step_description'	: "get_final_sequence",
				'status'			: status,
				'output'			: {
					'final_order_orientation_copy_number'	: final_order_orientation_copy_number,
					'final_sequence'						: str(final_sequence),
					'final_sequence_length'					: final_sequence_length
					}
				}
	if status != "PASS":
		write_log_and_exit(log, status)
	
	SeqIO.write(SeqRecord(Seq(final_sequence),gfaFile), log['00']['input']['sample_name'] + "_asm.fasta", "fasta")

	final_itr_length, status = get_itr_length( longest_contig ,final_path , original_graph.segments )
	log['10'] = {'step_name' 		: "get_itr_length",
				'step_description'	: "get_itr_length",
				'status'			: status,
				'output'			: {
					'final_itr_length'	: final_itr_length
					}
				}
	
	write_log_and_exit(log,status)
	
if __name__=='__main__':
	main(sys.argv[1:])
