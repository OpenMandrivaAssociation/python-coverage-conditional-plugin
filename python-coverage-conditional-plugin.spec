%define module coverage-conditional-plugin
%define oname coverage_conditional_plugin
%bcond_without test

Name:		python-coverage-conditional-plugin
Version:	0.9.0
Release:	2
Summary:	Conditional coverage based on any rules you define!
URL:		https://pypi.org/project/coverage-conditional-plugin/
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/c/coverage-conditional-plugin/%{oname}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(coverage)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(importlib-metadata)

%if %{with test}
BuildRequires:	python%{pyver}dist(poetry)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(mypy)
BuildRequires:	python%{pyver}dist(types-setuptools)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-cov)
BuildRequires:	python%{pyver}dist(pytest-randomly)
%endif

%description
Conditional coverage based on any rules you define!

Some projects have different parts that relies on different environments:

  Python version, some code is only executed on specific versions and
  ignored on others

  OS version, some code might be Windows, Mac, or Linux only

  External packages, some code is only executed when some 3rd party
  package is installed

Current best practice is to use # pragma: no cover for this places in
our project.

This project allows to use configurable pragmas that include code to the
coverage if some condition evaluates to true, and fallback to ignoring
this code when condition is false.


%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%py_build

%install
%py3_install

%if %{with test}
%check
# skip baize tests, not packaged
ignore='not test_integration'
%{__python} -m pytest --import-mode append -v tests/ -k "$ignore"
%endif

%files
%{python3_sitelib}/%{oname}
%{python3_sitelib}/%{oname}-%{version}.dist-info
%license LICENSE