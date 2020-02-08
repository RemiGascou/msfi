
MODULENAME=msfi

all : clean build

.PHONY: clean
clean :
	@rm -rf `find ./ -type d -name "*__pycache__"`
	@if [ -d "./dist/" ]; then rm -rf "./dist/"; fi
	@if [ -d "./build/" ]; then rm -rf "./build/"; fi
	@if [ -d "./${MODULENAME}.egg-info/" ]; then rm -rf "./${MODULENAME}.egg-info/"; fi

build :
	@echo "[BUILD] python3 setup.py sdist bdist_wheel"
	@python3 ./${MODULENAME}/setup.py sdist bdist_wheel

upload : build
	@if [ $(shell python3 -m pip list | grep twine | wc -l) -eq '0' ]; then \
		echo "[UPLOAD] Installing required python3 package twine ..."; 		\
		python3 -m pip install twine; 										\
	fi
	@python3 setup.py sdist
	@python3 -m twine upload "./dist/*"

install: build
	@if [ -d "./${MODULENAME}/requirements.txt" ]; then python3 -m pip install -r ./${MODULENAME}/requirements.txt ; fi
	@python3 -m pip install ../msfi/${MODULENAME}

uninstall:
	@python3 -m pip uninstall ${MODULENAME}

release :
	@if [ ! -d "./releases/" ]; then mkdir -p "./releases/"; fi
	@if [ -f ./dist/${MODULENAME}*.whl ]; then 				\
		echo "[RELEASE] Copying release : $(shell basename ./dist/${MODULENAME}*.whl)"; 	\
		cp ./dist/${MODULENAME}*.whl "./releases/"; 		\
	fi
