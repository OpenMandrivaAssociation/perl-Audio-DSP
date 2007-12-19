%define module	Audio-DSP
%define name	perl-%{module}
%define version 0.02
%define release %mkrel 10

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl interface to OSS digital audio device
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Audio/%{module}-%{version}.tar.bz2
Patch0:		Audio-DSP-0.02-VOCP.patch
Url:		http://search.cpan.org/dist/%{module}/
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

%setup -q -n %{module}-%{version} 
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
# doesn't work

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



