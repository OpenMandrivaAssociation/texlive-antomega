%global tl_name antomega
%global tl_revision 21933

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8
Release:	%{tl_revision}.1
Summary:	Alternative language support for Omega/Lambda
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/obsolete/systems/omega/contrib/antomega
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/antomega.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/antomega.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/antomega.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(omega)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A language support package for Omega/Lambda. This replaces the original
omega package for use with Lambda, and provides extra facilities
(including Babel-like language switching, which eases porting of LaTeX
documents to Lambda).

