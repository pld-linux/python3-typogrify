Summary:	Filters to enhance web typography, including support for Django & Jinja templates
Summary(pl.UTF-8):	Filtry rozszerzające typografię WWW z obsługą szablonów Django i Jinja
Name:		python3-typogrify
Version:	2.1.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/typogrify/
Source0:	https://files.pythonhosted.org/packages/source/t/typogrify/typogrify-%{version}.tar.gz
# Source0-md5:	7cc9a0a1de988329add3982519dc7971
URL:		https://pypi.org/project/typogrify/
BuildRequires:	python3-build
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
BuildRequires:	sed >= 4.0
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Typogrify provides a set of custom filters that automatically apply
various transformations to plain text in order to yield
typographically-improved HTML. While often used in conjunction with
Jinja and Django template systems, the filters can be used in any
environment.

%description -l pl.UTF-8
Typogrify udostępnia zestaw dostosowanych filtrów, automatycznie
nakładających na czysty tekst różne przekształcenia, aby wytworzyć
typograficznie ulepszony HTML. Filtry zwykle używane są wraz z
systemami szablonów Jinja i Django, ale można ich używać w dowolnym
środowisku.

%prep
%setup -q -n typogrify-%{version}

# actually not executable
%{__sed} -i -e '/^#!\/usr\/bin\/env python/d' typogrify/packages/titlecase/__init__.py

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE.txt README.md
%{py3_sitescriptdir}/typogrify
%{py3_sitescriptdir}/typogrify-%{version}.dist-info
