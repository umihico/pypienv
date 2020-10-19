pypi_common:
	docker build . -t umihico/pypienv_$(dir_name) -f pypi/Dockerfile
	touch $(dir_name)/__version__.py
	docker run --rm \
		--mount type=bind,source=$(shell pwd)/$(dir_name)/__version__.py,target=/app/$(dir_name)/__version__.py \
		-e AWS_ACCESS_KEY_ID=$(shell aws configure get aws_access_key_id) \
		-e AWS_SECRET_ACCESS_KEY=$(shell aws configure get aws_secret_access_key) \
		-e AWS_DEFAULT_REGION=$(shell aws configure get region) \
		umihico/pypienv_$(dir_name) make _pypi_$(stage) pip_name=example-pkg-umihico dir_name=$(dir_name)
_pypi_common:
	PKG_NAME=$(pip_name) DIR_NAME=$(dir_name) STAGE=$(stage) python define_version.py
	PKG_NAME=$(pip_name) DIR_NAME=$(dir_name) STAGE=$(stage) python setup.py bdist_wheel
pypi_stg:
	@make pypi_common stage=stg dir_name=example_pkg_umihico
_pypi_stg:
	@make _pypi_common stage=stg pip_name=$(pip_name)
	PKG_NAME=$(pip_name) twine upload --repository testpypi dist/* \
	-u $(shell aws ssm get-parameter --name PYPI_USERNAME_TEST --query 'Parameter.Value' --output text) \
	-p $(shell aws ssm get-parameter --name PYPI_PASSWORD_TEST --query 'Parameter.Value' --output text)
	PKG_NAME=$(pip_name) python pip_install.py stg
pypi_prod:
	@make pypi_common stage=prod dir_name=example_pkg_umihico
_pypi_prod:
	@make _pypi_common stage=prod
	PKG_NAME=$(pip_name) twine upload dist/* \
	-u $(shell aws ssm get-parameter --name PYPI_USERNAME_PROD --query 'Parameter.Value' --output text) \
	-p $(shell aws ssm get-parameter --name PYPI_PASSWORD_PROD --query 'Parameter.Value' --output text)
	PKG_NAME=$(pip_name) python pip_install.py prod
