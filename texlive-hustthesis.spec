%global tl_name hustthesis
%global tl_revision 78285

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1.0
Release:	%{tl_revision}.1
Summary:	Unofficial thesis template for Huazhong University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/hustthesis
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hustthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hustthesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hustthesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an Unofficial Thesis Template in LaTeX for Huazhong
University of Science and Technology.

