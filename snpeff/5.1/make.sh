#!/bin/sh -e

export SNPEFF_VERSION=5.1d
export SNPEFF_MVN_POM_VERSION=5.1
export SNPSIFT_VERSION=5.1

# Separate version-subversion by '_'
# E.g.: '4_1' (instead of '4.1')
export VERSION_UND=`echo $VERSION | tr '.' '_'`

#---
# Build SnpEff
#---

cd /SnpEff-$SNPEFF_VERSION

mvn clean compile assembly:single jar:jar

cp target/SnpEff-$SNPEFF_MVN_POM_VERSION-jar-with-dependencies.jar /SnpEff-$SNPEFF_VERSION/snpEff.jar

# Install JAR file in local Maven repo
mvn install:install-file \
	-Dfile=target/SnpEff-$SNPEFF_MVN_POM_VERSION.jar \
	-DgroupId=org.snpeff \
	-DartifactId=SnpEff \
	-Dversion=$SNPEFF_MVN_POM_VERSION \
	-Dpackaging=jar \
	-DgeneratePom=true \
	--quiet

cd - 

#---
# Build SnpSift
#---
cd /SnpSift-$SNPSIFT_VERSION

mvn clean compile assembly:single jar:jar

cp target/SnpSift-$SNPSIFT_VERSION-jar-with-dependencies.jar /SnpEff-$SNPEFF_VERSION/SnpSift.jar

# Install JAR file in local Maven repo
mvn install:install-file \
	-Dfile=target/SnpSift-$SNPSIFT_VERSION.jar \
	-DgroupId=org.snpsift \
	-DartifactId=SnpSift \
	-Dversion=$SNPSIFT_VERSION \
	-Dpackaging=jar \
	-DgeneratePom=true \
	--quiet

cd - 

#---
# Update galaxy databases
#---
bash galaxy.sh

echo "Build done!"
