%include	/usr/lib/rpm/macros.php
%define		_class		MIME
%define		_subclass	Type
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - utility class for dealing with MIME types
Summary(pl):	%{_pearname} - przydatna klasa do obs³ugi typów MIME
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	dc2d377a121c6410d5f5c46e8ec32c03
URL:		http://pear.php.net/package/MIME_Type/
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
- Autodetect a file's MIME-type, either with mime_content_type() or
  the 'file' command.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa dostarcza funkcjonalno¶ci do obs³ugi typów MIME:
- przetwarzanie typu MIME,
- pe³na obs³uga specyfikacji RFC2045
- wiele przydatnych funkcji do obs³ugi i okre¶lania informacji na
  temat typów
- wiêkszo¶æ funkcji mo¿e byæ wywo³ana statycznie
- autodetekecja typu MIME pliku, za pomoc± mime_content_type() lub
  z wykorzystaniem polecenia 'file'.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/Type.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/Parameter.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/example.php
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
