Name:		texlive-antomega
Version:	21933
Release:	2
Summary:	Alternative language support for Omega/Lambda
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/omega/contrib/antomega
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/antomega.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/antomega.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/antomega.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-omega

%description
A language support package for Omega/Lambda. This replaces the
original omega package for use with Lambda, and provides extra
facilities (including Babel-like language switching, which
eases porting of LaTeX documents to Lambda).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/omega/ocp/antomega/babel2de.ocp
%{_texmfdistdir}/omega/ocp/antomega/babel2es.ocp
%{_texmfdistdir}/omega/ocp/antomega/babel2la.ocp
%{_texmfdistdir}/omega/ocp/antomega/babel2pl.ocp
%{_texmfdistdir}/omega/ocp/antomega/babel2punct.ocp
%{_texmfdistdir}/omega/ocp/antomega/babel2ru.ocp
%{_texmfdistdir}/omega/ocp/antomega/bblgrk2uni.ocp
%{_texmfdistdir}/omega/ocp/antomega/dosrus2uni.ocp
%{_texmfdistdir}/omega/ocp/antomega/greek2punct.ocp
%{_texmfdistdir}/omega/ocp/antomega/iso2uni.ocp
%{_texmfdistdir}/omega/ocp/antomega/isobaltic2uni.ocp
%{_texmfdistdir}/omega/ocp/antomega/isoce2uni.ocp
%{_texmfdistdir}/omega/ocp/antomega/isocyr2uni.ocp
%{_texmfdistdir}/omega/ocp/antomega/isogrk2uni.ocp
%{_texmfdistdir}/omega/ocp/antomega/koirus2uni.ocp
%{_texmfdistdir}/omega/ocp/antomega/latcyr2uni.ocp
%{_texmfdistdir}/omega/ocp/antomega/latin/la-lig.ocp
%{_texmfdistdir}/omega/ocp/antomega/latin/la-longs.ocp
%{_texmfdistdir}/omega/ocp/antomega/latin/la-noj.ocp
%{_texmfdistdir}/omega/ocp/antomega/latin/la-nouv.ocp
%{_texmfdistdir}/omega/ocp/antomega/oldstyle.ocp
%{_texmfdistdir}/omega/ocp/antomega/rhobre.ocp
%{_texmfdistdir}/omega/ocp/antomega/rhonobre.ocp
%{_texmfdistdir}/omega/ocp/antomega/tex2punct.ocp
%{_texmfdistdir}/omega/ocp/antomega/texgrk2uni.ocp
%{_texmfdistdir}/omega/ocp/antomega/uni2accents.ocp
%{_texmfdistdir}/omega/ocp/antomega/uni2lgr.ocp
%{_texmfdistdir}/omega/ocp/antomega/uni2lig.ocp
%{_texmfdistdir}/omega/ocp/antomega/uni2omega.ocp
%{_texmfdistdir}/omega/ocp/antomega/uni2t1.ocp
%{_texmfdistdir}/omega/ocp/antomega/uni2t2a.ocp
%{_texmfdistdir}/omega/ocp/antomega/uniutf2uni.ocp
%{_texmfdistdir}/omega/ocp/antomega/uppercase-dflt.ocp
%{_texmfdistdir}/omega/ocp/antomega/win2uni.ocp
%{_texmfdistdir}/omega/ocp/antomega/winbaltic2uni.ocp
%{_texmfdistdir}/omega/ocp/antomega/wince2uni.ocp
%{_texmfdistdir}/omega/ocp/antomega/wincyr2uni.ocp
%{_texmfdistdir}/omega/otp/antomega/babel2de.otp
%{_texmfdistdir}/omega/otp/antomega/babel2es.otp
%{_texmfdistdir}/omega/otp/antomega/babel2la.otp
%{_texmfdistdir}/omega/otp/antomega/babel2pl.otp
%{_texmfdistdir}/omega/otp/antomega/babel2punct.otp
%{_texmfdistdir}/omega/otp/antomega/babel2ru.otp
%{_texmfdistdir}/omega/otp/antomega/bblgrk2uni.otp
%{_texmfdistdir}/omega/otp/antomega/dosrus2uni.otp
%{_texmfdistdir}/omega/otp/antomega/greek2punct.otp
%{_texmfdistdir}/omega/otp/antomega/iso2uni.otp
%{_texmfdistdir}/omega/otp/antomega/isobaltic2uni.otp
%{_texmfdistdir}/omega/otp/antomega/isoce2uni.otp
%{_texmfdistdir}/omega/otp/antomega/isocyr2uni.otp
%{_texmfdistdir}/omega/otp/antomega/isogrk2uni.otp
%{_texmfdistdir}/omega/otp/antomega/koirus2uni.otp
%{_texmfdistdir}/omega/otp/antomega/latcyr2uni.otp
%{_texmfdistdir}/omega/otp/antomega/latin/la-lig.otp
%{_texmfdistdir}/omega/otp/antomega/latin/la-longs.otp
%{_texmfdistdir}/omega/otp/antomega/latin/la-noj.otp
%{_texmfdistdir}/omega/otp/antomega/latin/la-nouv.otp
%{_texmfdistdir}/omega/otp/antomega/rhobre.otp
%{_texmfdistdir}/omega/otp/antomega/rhonobre.otp
%{_texmfdistdir}/omega/otp/antomega/tex2punct.otp
%{_texmfdistdir}/omega/otp/antomega/texgrk2uni.otp
%{_texmfdistdir}/omega/otp/antomega/uni2accents.otp
%{_texmfdistdir}/omega/otp/antomega/uni2lgr.otp
%{_texmfdistdir}/omega/otp/antomega/uni2lig.otp
%{_texmfdistdir}/omega/otp/antomega/uni2omega.otp
%{_texmfdistdir}/omega/otp/antomega/uni2t1.otp
%{_texmfdistdir}/omega/otp/antomega/uni2t2a.otp
%{_texmfdistdir}/omega/otp/antomega/uniutf2uni.otp
%{_texmfdistdir}/omega/otp/antomega/uppercase-dflt.otp
%{_texmfdistdir}/omega/otp/antomega/win2uni.otp
%{_texmfdistdir}/omega/otp/antomega/winbaltic2uni.otp
%{_texmfdistdir}/omega/otp/antomega/wince2uni.otp
%{_texmfdistdir}/omega/otp/antomega/wincyr2uni.otp
%{_texmfdistdir}/tex/lambda/antomega/antomega.cfg
%{_texmfdistdir}/tex/lambda/antomega/antomega.sty
%{_texmfdistdir}/tex/lambda/antomega/grhyph16.tex
%{_texmfdistdir}/tex/lambda/antomega/hyphen.cfg
%{_texmfdistdir}/tex/lambda/antomega/language.dat.sample
%{_texmfdistdir}/tex/lambda/antomega/lgc0700.def
%{_texmfdistdir}/tex/lambda/antomega/lgrenc-antomega.def
%{_texmfdistdir}/tex/lambda/antomega/ograhyph4.tex
%{_texmfdistdir}/tex/lambda/antomega/ogrmhyph4.tex
%{_texmfdistdir}/tex/lambda/antomega/ogrphyph4.tex
%{_texmfdistdir}/tex/lambda/antomega/omega-english.ldf
%{_texmfdistdir}/tex/lambda/antomega/omega-french.ldf
%{_texmfdistdir}/tex/lambda/antomega/omega-german.ldf
%{_texmfdistdir}/tex/lambda/antomega/omega-greek.ldf
%{_texmfdistdir}/tex/lambda/antomega/omega-latin.ldf
%{_texmfdistdir}/tex/lambda/antomega/omega-latvian.ldf
%{_texmfdistdir}/tex/lambda/antomega/omega-polish.ldf
%{_texmfdistdir}/tex/lambda/antomega/omega-russian.ldf
%{_texmfdistdir}/tex/lambda/antomega/omega-spanish.ldf
%{_texmfdistdir}/tex/lambda/antomega/ruhyph16.tex
%{_texmfdistdir}/tex/lambda/antomega/t1enc-antomega.def
%{_texmfdistdir}/tex/lambda/antomega/t2aenc-antomega.def
%{_texmfdistdir}/tex/lambda/antomega/uni0100.def
%{_texmfdistdir}/tex/lambda/antomega/uni0370.def
%{_texmfdistdir}/tex/lambda/antomega/uni0400.def
%{_texmfdistdir}/tex/lambda/antomega/uni1f00.def
%{_texmfdistdir}/tex/lambda/antomega/ut1enc-antomega.def
%doc %{_texmfdistdir}/doc/omega/antomega/README
%doc %{_texmfdistdir}/doc/omega/antomega/antomega.pdf
#- source
%doc %{_texmfdistdir}/source/lambda/antomega/antenc.dtx
%doc %{_texmfdistdir}/source/lambda/antomega/antenc.ins
%doc %{_texmfdistdir}/source/lambda/antomega/antomega.dtx
%doc %{_texmfdistdir}/source/lambda/antomega/antomega.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar omega tex doc source %{buildroot}%{_texmfdistdir}
