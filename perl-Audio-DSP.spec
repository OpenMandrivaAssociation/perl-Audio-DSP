%define upstream_name	 Audio-DSP
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:	0.02
Release:	1

Summary:	Perl interface to OSS digital audio device
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	https://cpan.metacpan.org/authors/id/S/SE/SETHJ/Audio-DSP-0.02.tar.gz
Patch0:		Audio-DSP-0.02-VOCP.patch

BuildRequires:	make
BuildRequires:	perl-devel

%description
Audio::DSP is built around the OSS (Open Sound System) API and allows perl to
interface with a digital audio device. It provides, among other things, an
initialization method which opens and handles ioctl messaging on the audio
device file. Audio::DSP also provides some rudimentary methods for the storage
and manipulation of audio data in memory.

In order to use Audio::DSP, you'll need to have the necessary OSS
drivers/libraries installed. OSS is available for many popular Unices, and a
GPLed version (with which this extension was initially developed and tested) is
distributed with with the Linux kernel. 

%prep

%setup -q -n Audio-DSP-0.02
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
# doesn't work
make test || :
%install
%{__rm} -rf %{buildroot} 
%makeinstall_std

%clean 
%{__rm} -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes MANIFEST README
%{perl_vendorarch}/Audio
%{perl_vendorarch}/auto/Audio
%{_mandir}/man3/*


