%define fontname lato

%define fontdir		%{_datadir}/fonts/TTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	A sanserif type­face font fam­ily
Name:		fonts-ttf-%{fontname}
Version:	2.015
Release:	0
Url:		https://www.latofonts.com/
License:	OFL
Group:		System/Fonts/True type
# Last updated: August 6th, 2015
# wget https://www.latofonts.com/download/Lato2OFL.zip
# unzip Lato2OFL.zip
# mv Lato2OFL fonts-ttf-lato-2.015
# tar -cJ --exclude __MACOSX -f fonts-ttf-lato-2.015.tar.xz fonts-ttf-lato-2.015/
Source0:	%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	fontconfig
BuildRequires:	mkfontscale
BuildRequires:	mkfontdir

%description
Lato is a sanserif typeface family designed in the Summer 2010 and extended
in the Summer 2013 by Warsaw-based designer Lukasz Dziedzic ("Lato" means
"Summer" in Polish).

It tries to carefully balance some potentially conflicting priorities: it
should seem quite "transparent" when used in body text but would display
some original traits when used in larger sizes. The classical proportions,
particularly visible in the uppercase, give the letterforms familiar harmony
and elegance. At the same time, its sleek sanserif look makes evident the
fact that Lato was designed in the 2010s, even though it does not follow any
current trend.

The semi-rounded details of the letters give Lato a feeling of warmth, while
the strong structure provides stability and seriousness. In 2013-2014, the
family was greatly extended (with the help of Adam Twardoch and Botio
Nikoltchev) to cover 3000+ glyphs over nine weights with italics. It now
supports 100+ Latin-based languages, 50+ Cyrillic-based languages as well as
Greek and IPA phonetics.

%prep
%setup -q -n %{name}-%{version}

%build
# nothing to do here!

%install
install -dm 0755 %{buildroot}/%{fontdir}/
install -pm 0644 *.ttf %{buildroot}/%{fontdir}/

#ttmkfdir %{buildroot}%{buildroot}%{fontdir}/ > %{buildroot}%{buildroot}%{fontdir}/fonts.dir
#ln -s fonts.dir %{buildroot}%{buildroot}%{fontdir}//fonts.scale
#

mkfontscale %{buildroot}%{fontdir}/
mkfontdir %{buildroot}%{fontdir}/

mkdir -p %{buildroot}%{fontconfdir}/
ln -s ../../..%{buildroot}%{fontdir} %{buildroot}%{fontconfdir}/ttf-%{fontname}:pri=50

%files
%dir %{fontdir}
%{fontconfdir}/ttf-%{fontname}:pri=50
%{fontdir}/*.ttf
%verify(not mtime)%{fontdir}/fonts.dir
%{fontdir}/fonts.scale
%doc README.txt
%doc OFL.txt

