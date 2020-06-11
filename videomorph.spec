Name:           videomorph
Version:        1.4.1
Release:        2%{?dist}
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


%if 0%{?fedora} >= 33
BuildRequires:  python3.8-devel
BuildRequires:	python3.8-qt5
Requires:	python3.8
Requires:	python3.8-qt5
%else
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3-rpm-macros
%endif
BuildRequires:	python3-qt5-devel
BuildRequires:	ffmpeg
BuildRequires:	ffmpeg-devel
Requires:	ffmpeg

%prep
%autosetup -n videomorph-%{version}  


# Change shebang in all relevant files in this directory and all subdirectories
# See `man find` for how the `-exec command {} +` syntax works
%if 0%{?fedora} >= 33
find -depth -type f -writable -name "*.py" -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!/usr/bin/python3.8=' {} +
%else
find -type f -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +
%endif

%build
%if 0%{?fedora} >= 33
python3.8 setup.py build
%else
%py3_build
%endif

%install
%if 0%{?fedora} >= 33
python3.8 setup.py install --root=%{buildroot} --optimize=1 --skip-build
%else
%py3_install
%endif 

%files 

%{_bindir}/videomorph
%if 0%{?fedora} >= 33
/usr/lib/python3.8/site-packages/videomorph-*-py*.egg-info
/usr/lib/python3.8/site-packages/videomorph/
%else
%{python3_sitelib}/videomorph-*-py*.egg-info
%{python3_sitelib}/videomorph/
%endif
%{_datadir}/applications/videomorph.desktop
%{_docdir}/videomorph/
%{_datadir}/icons/videomorph.png
%{_mandir}/man1/videomorph.*.gz
%{_datadir}/videomorph/



%changelog

* Tue Jun 02 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.4.1-2
- Rebuilt for python3.9

* Sat Nov 30 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.4.1-1
- Initial build
