Name:		texlive-context-fancybreak
Version:	47085
Release:	1
Summary:	Overfull pages with ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/context-fancybreak
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-fancybreak.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-fancybreak.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The (ConTeXt) module allows insertion of thought breaks in
texts. With parameters one can adjust the spacing around the
content and set a default symbol.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex
%{_texmfdistdir}/tex/context
%{_texmfdistdir}/tex/context/third
%{_texmfdistdir}/tex/context/third/fancybreak
%{_texmfdistdir}/tex/context/third/fancybreak/t-fancybreak.mkvi
%{_texmfdistdir}/tex/context/third/fancybreak/t-fancybreak.mkii
%{_texmfdistdir}/tex/context/interface
%{_texmfdistdir}/tex/context/interface/third
%{_texmfdistdir}/tex/context/interface/third/t-fancybreak.xml
%{_texmfdistdir}/doc
%doc %{_texmfdistdir}/doc/context
%doc %{_texmfdistdir}/doc/context/third
%doc %{_texmfdistdir}/doc/context/third/fancybreak
%doc %{_texmfdistdir}/doc/context/third/fancybreak/fancybreak-doc.pdf
%doc %{_texmfdistdir}/doc/context/third/fancybreak/VERSION
%doc %{_texmfdistdir}/doc/context/third/fancybreak/README

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
