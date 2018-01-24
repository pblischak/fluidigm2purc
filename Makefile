.PHONY : deps install uninstall clean pear test

deps :
	@# Make dependencies directory
	@mkdir deps

	@# Clone and compile flahs2
	@printf "\n**** Cloning flash2 from GitHub ****\n\n"
	git clone https://github.com/dstreett/FLASH2.git deps/flash_dir
	@printf "\n**** Compiling flash2 ****\n\n"
	@cd deps/flash_dir; make; mv flash2 ..
	@rm -rf deps/flash_dir

	@# Clone and compile sickle
	@printf "\n**** Cloning sickle from GitHub ****\n\n"
	git clone https://github.com/najoshi/sickle.git deps/sickle_dir
	@printf "\n**** Compiling sickle ****\n\n"
	@cd deps/sickle_dir; make; mv sickle ..
	@rm -rf deps/sickle_dir

pear :
	@# Clone and compile pear
	@printf "\n**** Cloning pear from GitHub ****\n\n"
	git clone https://github.com/xflouris/PEAR.git deps/pear_dir
	@printf "\n**** Compiling pear ****\n\n"
	@cd deps/pear_dir; ./autogen.sh; ./configure; make; mv src/pear ..
	@rm -rf deps/pear_dir

install :
	@cp deps/sickle deps/flash2 fluidigm2purc crunch_clusters /usr/local/bin
	@#export PATH=$PATH:$(pwd)
	@#CURDIR=$(pwd)
	@#printf "\nTo keep these scripts in your \044PATH, add\n\nexport PATH=\044PATH:${CURDIR}\n\nto your .bash_profile.\n\n"

uninstall :
	@rm -i /usr/local/bin/sickle /usr/local/bin/flash2 /usr/local/bin/pear /usr/local/bin/fluidigm2purc /usr/local/bin/crunch_clusters

clean :
	@rm -rf deps

test :
	@sickle pe --help
	@flash2 --help
	@fluidigm2purc -h
	@crunch_clusters -h
	@cd tests; fluidigm2purc -f TEST
