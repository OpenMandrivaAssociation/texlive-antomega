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
Requires(pre):	texlive-tlpkg
Requires:	texlive(omega)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A language support package for Omega/Lambda. This replaces the original
omega package for use with Lambda, and provides extra facilities
(including Babel-like language switching, which eases porting of LaTeX
documents to Lambda).

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/omega
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/omega
%dir %{_datadir}/texmf-dist/omega/ocp
%dir %{_datadir}/texmf-dist/omega/otp
%dir %{_datadir}/texmf-dist/source/lambda
%dir %{_datadir}/texmf-dist/tex/lambda
%dir %{_datadir}/texmf-dist/doc/omega/antomega
%dir %{_datadir}/texmf-dist/omega/ocp/antomega
%dir %{_datadir}/texmf-dist/omega/otp/antomega
%dir %{_datadir}/texmf-dist/source/lambda/antomega
%dir %{_datadir}/texmf-dist/tex/lambda/antomega
%dir %{_datadir}/texmf-dist/omega/ocp/antomega/latin
%dir %{_datadir}/texmf-dist/omega/otp/antomega/latin
%doc %{_datadir}/texmf-dist/doc/omega/antomega/README
%doc %{_datadir}/texmf-dist/doc/omega/antomega/antomega.pdf
%{_datadir}/texmf-dist/omega/ocp/antomega/babel2de.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/babel2es.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/babel2la.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/babel2pl.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/babel2punct.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/babel2ru.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/bblgrk2uni.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/dosrus2uni.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/greek2punct.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/iso2uni.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/isobaltic2uni.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/isoce2uni.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/isocyr2uni.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/isogrk2uni.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/koirus2uni.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/latcyr2uni.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/latin/la-lig.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/latin/la-longs.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/latin/la-noj.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/latin/la-nouv.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/oldstyle.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/rhobre.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/rhonobre.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/tex2punct.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/texgrk2uni.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/uni2accents.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/uni2lgr.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/uni2lig.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/uni2omega.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/uni2t1.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/uni2t2a.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/uniutf2uni.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/uppercase-dflt.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/win2uni.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/winbaltic2uni.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/wince2uni.ocp
%{_datadir}/texmf-dist/omega/ocp/antomega/wincyr2uni.ocp
%{_datadir}/texmf-dist/omega/otp/antomega/babel2de.otp
%{_datadir}/texmf-dist/omega/otp/antomega/babel2es.otp
%{_datadir}/texmf-dist/omega/otp/antomega/babel2la.otp
%{_datadir}/texmf-dist/omega/otp/antomega/babel2pl.otp
%{_datadir}/texmf-dist/omega/otp/antomega/babel2punct.otp
%{_datadir}/texmf-dist/omega/otp/antomega/babel2ru.otp
%{_datadir}/texmf-dist/omega/otp/antomega/bblgrk2uni.otp
%{_datadir}/texmf-dist/omega/otp/antomega/dosrus2uni.otp
%{_datadir}/texmf-dist/omega/otp/antomega/greek2punct.otp
%{_datadir}/texmf-dist/omega/otp/antomega/iso2uni.otp
%{_datadir}/texmf-dist/omega/otp/antomega/isobaltic2uni.otp
%{_datadir}/texmf-dist/omega/otp/antomega/isoce2uni.otp
%{_datadir}/texmf-dist/omega/otp/antomega/isocyr2uni.otp
%{_datadir}/texmf-dist/omega/otp/antomega/isogrk2uni.otp
%{_datadir}/texmf-dist/omega/otp/antomega/koirus2uni.otp
%{_datadir}/texmf-dist/omega/otp/antomega/latcyr2uni.otp
%{_datadir}/texmf-dist/omega/otp/antomega/latin/la-lig.otp
%{_datadir}/texmf-dist/omega/otp/antomega/latin/la-longs.otp
%{_datadir}/texmf-dist/omega/otp/antomega/latin/la-noj.otp
%{_datadir}/texmf-dist/omega/otp/antomega/latin/la-nouv.otp
%{_datadir}/texmf-dist/omega/otp/antomega/rhobre.otp
%{_datadir}/texmf-dist/omega/otp/antomega/rhonobre.otp
%{_datadir}/texmf-dist/omega/otp/antomega/tex2punct.otp
%{_datadir}/texmf-dist/omega/otp/antomega/texgrk2uni.otp
%{_datadir}/texmf-dist/omega/otp/antomega/uni2accents.otp
%{_datadir}/texmf-dist/omega/otp/antomega/uni2lgr.otp
%{_datadir}/texmf-dist/omega/otp/antomega/uni2lig.otp
%{_datadir}/texmf-dist/omega/otp/antomega/uni2omega.otp
%{_datadir}/texmf-dist/omega/otp/antomega/uni2t1.otp
%{_datadir}/texmf-dist/omega/otp/antomega/uni2t2a.otp
%{_datadir}/texmf-dist/omega/otp/antomega/uniutf2uni.otp
%{_datadir}/texmf-dist/omega/otp/antomega/uppercase-dflt.otp
%{_datadir}/texmf-dist/omega/otp/antomega/win2uni.otp
%{_datadir}/texmf-dist/omega/otp/antomega/winbaltic2uni.otp
%{_datadir}/texmf-dist/omega/otp/antomega/wince2uni.otp
%{_datadir}/texmf-dist/omega/otp/antomega/wincyr2uni.otp
%doc %{_datadir}/texmf-dist/source/lambda/antomega/antenc.dtx
%doc %{_datadir}/texmf-dist/source/lambda/antomega/antenc.ins
%doc %{_datadir}/texmf-dist/source/lambda/antomega/antomega.dtx
%doc %{_datadir}/texmf-dist/source/lambda/antomega/antomega.ins
%{_datadir}/texmf-dist/tex/lambda/antomega/antomega.cfg
%{_datadir}/texmf-dist/tex/lambda/antomega/antomega.sty
%{_datadir}/texmf-dist/tex/lambda/antomega/grhyph16.tex
%{_datadir}/texmf-dist/tex/lambda/antomega/hyphen.cfg
%{_datadir}/texmf-dist/tex/lambda/antomega/language.dat.sample
%{_datadir}/texmf-dist/tex/lambda/antomega/lgc0700.def
%{_datadir}/texmf-dist/tex/lambda/antomega/lgrenc-antomega.def
%{_datadir}/texmf-dist/tex/lambda/antomega/ograhyph4.tex
%{_datadir}/texmf-dist/tex/lambda/antomega/ogrmhyph4.tex
%{_datadir}/texmf-dist/tex/lambda/antomega/ogrphyph4.tex
%{_datadir}/texmf-dist/tex/lambda/antomega/omega-english.ldf
%{_datadir}/texmf-dist/tex/lambda/antomega/omega-french.ldf
%{_datadir}/texmf-dist/tex/lambda/antomega/omega-german.ldf
%{_datadir}/texmf-dist/tex/lambda/antomega/omega-greek.ldf
%{_datadir}/texmf-dist/tex/lambda/antomega/omega-latin.ldf
%{_datadir}/texmf-dist/tex/lambda/antomega/omega-latvian.ldf
%{_datadir}/texmf-dist/tex/lambda/antomega/omega-polish.ldf
%{_datadir}/texmf-dist/tex/lambda/antomega/omega-russian.ldf
%{_datadir}/texmf-dist/tex/lambda/antomega/omega-spanish.ldf
%{_datadir}/texmf-dist/tex/lambda/antomega/ruhyph16.tex
%{_datadir}/texmf-dist/tex/lambda/antomega/t1enc-antomega.def
%{_datadir}/texmf-dist/tex/lambda/antomega/t2aenc-antomega.def
%{_datadir}/texmf-dist/tex/lambda/antomega/uni0100.def
%{_datadir}/texmf-dist/tex/lambda/antomega/uni0370.def
%{_datadir}/texmf-dist/tex/lambda/antomega/uni0400.def
%{_datadir}/texmf-dist/tex/lambda/antomega/uni1f00.def
%{_datadir}/texmf-dist/tex/lambda/antomega/ut1enc-antomega.def
