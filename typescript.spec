Summary:	TypeScript programming language
Name:		typescript
Version:	5.8.3
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	https://github.com/microsoft/TypeScript/releases/download/v%{version}/%{name}-%{version}.tgz
# Source0-md5:	823004e76ca78f972a429156c829e9d6
URL:		https://www.typescriptlang.org
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TypeScript is a language for application-scale JavaScript. TypeScript
adds optional types to JavaScript that support tools for large-scale
JavaScript applications for any browser, for any host, on any OS.
TypeScript compiles to readable, standards-based JavaScript.

%prep
%setup -qc

%{__mv} package/* .

%{__sed} -i -e '1 s,#!.*env node,#!/usr/bin/node,' bin/{tsc,tsserver}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{nodejs_libdir}/typescript}
cp -pr bin lib package.json $RPM_BUILD_ROOT%{nodejs_libdir}/typescript

%{__ln_s} %{nodejs_libdir}/typescript/bin/{tsc,tsserver} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_bindir}/tsc
%{_bindir}/tsserver
%dir %{nodejs_libdir}/typescript
%dir %{nodejs_libdir}/typescript/bin
%attr(755,root,root) %{nodejs_libdir}/typescript/bin/tsc
%attr(755,root,root) %{nodejs_libdir}/typescript/bin/tsserver
%{nodejs_libdir}/typescript/lib
%{nodejs_libdir}/typescript/package.json
