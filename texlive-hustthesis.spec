Name:		texlive-hustthesis
Version:	42547
Release:	2
Summary:	Unofficial thesis template for Huazhong University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hustthesis
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hustthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hustthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hustthesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an Unofficial Thesis Template in LaTeX for
Huazhong University of Science and Technology.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hustthesis
%{_texmfdistdir}/tex/latex/hustthesis
%{_texmfdistdir}/bibtex/bst/hustthesis
%doc %{_texmfdistdir}/doc/latex/hustthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
