%include	/usr/lib/rpm/macros.php
%define		_class		MIME
%define		_subclass	Type
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
%define		_extraver	beta3

Summary:	%{_pearname} - utility class for dealing with MIME types
Summary(pl):	%{_pearname} - przydatna klasa do obs�ugi typ�w MIME
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	0.%{_extraver}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_extraver}.tgz
# Source0-md5:	1b03675c7fec240d2c0431e8094991ea
URL:		http://pear.php.net/package/Class_Subclass/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides functionality for dealing with MIME types.
- Parse MIME type.
- Supports full RFC2045 specification.
- Many utility functions for working with and determining info about
  types.
- Most functions can be called statically.
- Autodetect a file's mime-type, either with mime_content_type() or
  the 'file' command.

In PEAR status of this package is: %{_status}.

%description -l pl
Dostarcza funkcjonalno�ci do obs�ugi typ�w MIME.
- przetwarzanie typu MIME,
- pe�ne wsparcie dla specyfikacji w RFC2045
- wiele przydatnych funkcji do obs�ugi i okre�lania informacji na
  temat typ�w
- wi�kszo�� funkcji mo�e by� wywo�ana statycznie
- autodetekecja typu mime pliku, za pomoc� mime_content_type() lub
  z wykorzystaniem polecenia 'file'.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c -n %{name}-%{version}%{_extraver}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}%{_extraver}/{Parameter,Type}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}%{_extraver}/example.php
%{php_pear_dir}/%{_class}/*.php