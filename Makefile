.PHONY : deps clean

deps :
	@# Make dependencies directory
	@mkdir deps

	@# Clone and compile flahs2
	@printf "\n**** Cloning flash2 from GitHub ****\n\n"
	git clone https://github.com/dstreett/FLASH2.git deps/flash_dir
	@printf "\n**** Compiling flash2 ****\n\n"
	@cd deps/flash_dir; make; mv flash2 ..
	@rm -rf deps/flash_dir

	@# Clone and compile pear
	@printf "\n**** Cloning pear from GitHub ****\n\n"
	git clone https://github.com/xflouris/PEAR.git deps/pear_dir
	@printf "\n**** Compiling pear ****\n\n"
	@cd deps/pear_dir; ./autogen.sh; ./configure; make; mv src/pear ..
	@rm -rf deps/pear_dir

	@# Clone and compile sickle
	@printf "\n**** Cloning sickle from GitHub ****\n\n"
	git clone https://github.com/najoshi/sickle.git deps/sickle_dir
	@printf "\n**** Compiling sickle ****\n\n"
	@cd deps/sickle_dir; make; mv sickle ..
	@rm -rf deps/sickle_dir

clean :
	@rm -rf deps
