%define major 0
%define libname %mklibname xcb-cursor %{major}
%define devname %mklibname xcb-cursor -d

Summary:	xcb-util's xcb-cursor
Name:		xcb-util-cursor
Version:	0.1.2
Release:	1
Url:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
License:	MIT
Group:		System/X11
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-render)
BuildRequires:	pkgconfig(xcb-renderutil)
BuildRequires:	pkgconfig(xorg-macros)

%description
This is the libXcursor port to XCB.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	xcb-util-cursor library package
Group:		System/X11
Obsoletes:	%{_lib}xcb-util-cursor0 < 0.1.1-2

%description -n %{libname}
This is the libXcursor port to XCB.

%files -n %{libname}
%{_libdir}/libxcb-cursor.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	xcb-util-cursor development files
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{_lib}xcb-util-cursor-devel < 0.1.1-2

%description -n %{devname}
This pakcage includes the development files required to build software against
%{name}.

%files -n %{devname}
%doc ChangeLog NEWS README
%{_includedir}/xcb/*.h
%{_libdir}/libxcb-cursor.so
%{_libdir}/pkgconfig/xcb-cursor.pc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure --disable-static
%make

%install
%makeinstall_std

