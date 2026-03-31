%define module pygccxml

Name:		python-pygccxml
Version:	3.0.2
Release:	1
Summary:	Python package for easy C++ declarations navigation
License:	BSL-1.0
Group:		Development/Python
URL:		https://github.com/CastXML/pygccxml
Source0:	https://github.com/CastXML/pygccxml/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Python package for easy C++ declarations navigation.

%files
%doc README.rst CHANGELOG.md
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
