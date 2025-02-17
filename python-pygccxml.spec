Name:		python-pygccxml
Version:	2.6.1
Release:	1
Source0:	https://github.com/CastXML/pygccxml/archive/refs/tags/v%{version}/pygccxml-%{version}.tar.gz
Summary:	Python package for easy C++ declarations navigation
URL:		https://github.com/CastXML/pygccxml
License:	Boost
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Python package for easy C++ declarations navigation.

%prep
%autosetup -p1 -n pygccxml-%{version}

%files
%{py_sitedir}/pygccxml
%{py_sitedir}/pygccxml-*.*-info
%doc README.rst
%doc CHANGELOG.md
%doc LICENSE.rst
