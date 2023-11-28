from pycirclize import Circos
from pycirclize.utils import fetch_genbank_by_accid
from pycirclize.parser import Genbank

# Download `NC_002483` E.coli plasmid genbank
gbk_fetch_data = fetch_genbank_by_accid("NC_002483")
gbk = Genbank(gbk_fetch_data)

# Initialize Circos instance with genome size
circos = Circos(sectors={gbk.name: gbk.range_size})
circos.text(f"Escherichia coli K-12 plasmid F\n\n{gbk.name}", size=14)
circos.rect(r_lim=(90, 100), fc="lightgrey", ec="none", alpha=0.5)
sector = circos.sectors[0]

# Plot forward strand CDS
f_cds_track = sector.add_track((95, 100))
f_cds_feats = gbk.extract_features("CDS", target_strand=1)
f_cds_track.genomic_features(f_cds_feats, plotstyle="arrow", fc="salmon", lw=0.5)

# Plot reverse strand CDS
r_cds_track = sector.add_track((90, 95))
r_cds_feats = gbk.extract_features("CDS", target_strand=-1)
r_cds_track.genomic_features(r_cds_feats, plotstyle="arrow", fc="skyblue", lw=0.5)

# Plot 'gene' qualifier label if exists
labels, label_pos_list = [], []
for feat in gbk.extract_features("CDS"):
    start = int(str(feat.location.start))
    end = int(str(feat.location.end))
    label_pos = (start + end) / 2
    gene_name = feat.qualifiers.get("gene", [None])[0]
    if gene_name is not None:
        labels.append(gene_name)
        label_pos_list.append(label_pos)
f_cds_track.xticks(label_pos_list, labels, label_size=6, label_orientation="vertical")

# Plot xticks (interval = 10 Kb)
r_cds_track.xticks_by_interval(
    10000, outer=False, label_formatter=lambda v: f"{v/1000:.1f} Kb"
)

circos.savefig("example02.png")