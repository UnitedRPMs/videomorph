Name:           videomorph
Version:        1.4.1
Release:        1%{?dist}
Summary:        Small GUI wrapper for FFMPEG based on PyQt5
License:        ASL 2.0
URL:            https://github.com/videomorph-dev/videomorph
Source0:        https://github.com/videomorph-dev/videomorph/archive/%{version}.tar.gz
BuildArch:      noarch

%description
VideoMorph is a video converter based on ffmpeg, and written with Python 3, 
and PyQt5. With VideoMorph you can convert your favorite videos to the 
currently more popular video formats, like MPG, MP4, AVI, WEBM, DVD, VCD, 
FLV, MOV, OGV, and also extract the audio to a file with MP3 format.


BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildRequires:	python3-qt5-devel
BuildRequires:	ffmpeg-devel
Requires:	ffmpeg

%prep
%autosetup -n videomorph-%{version}  


find -type f -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

%build
%{py3_build}

%install

%{py3_install} 

%files 

%{_bindir}/videomorph
%{python3_sitelib}/videomorph-*-py*.egg-info
%{python3_sitelib}/videomorph/
%{_datadir}/applications/videomorph.desktop
 %{_docdir}/videomorph/
%{_datadir}/icons/videomorph.png
%{_mandir}/man1/videomorph.*.gz
%{_datadir}/videomorph/



%changelog

* Sat Nov 30 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.4.1-1
- Initial build
