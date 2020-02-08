PYTHONINTERPRETER := "python3"

MODULENAME=msfi

all : clean build

.PHONY: clean
clean :
	@rm -rf `find ./ -type d -name "*__pycache__"`
	@if [ -d "./dist/" ]; then rm -rf "./dist/"; fi
	@if [ -d "./build/" ]; then rm -rf "./build/"; fi
	@if [ -d "./${MODULENAME}.egg-info/" ]; then rm -rf "./${MODULENAME}.egg-info/"; fi

build :
	echo "[BUILD] python3 setup.py sdist"
	@python3 setup.py sdist
	echo "[BUILD] python3 setup.py bdist_wheel"
	@python3 setup.py bdist_wheel

upload : build
	python3 setup.py upload

install: build
	@if [ -d "./${MODULENAME}/requirements.txt" ]; then python3 -m pip install -r requirements.txt ; fi
	@python3 -m pip install .

uninstall:
	@python3 -m pip uninstall ${MODULENAME}

release :
	@if [ ! -d "./releases/" ]; then mkdir -p "./releases/"; fi
	@if [ -f ./dist/${MODULENAME}*.whl ]; then 				\
		cp ./dist/${MODULENAME}*.whl "./releases/"; 		\
		echo "[RELEASE] Copying release : $(shell basename ./dist/${MODULENAME}*.whl)"; 	\
	fi
