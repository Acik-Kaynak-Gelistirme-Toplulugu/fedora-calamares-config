Name:           calamares
Version:        3.3.14
Release:        7%{?dist}
Summary:        Installer from a live CD/DVD/USB to disk

License:        GPL-3.0-or-later
URL:            https://calamares.io/
Source0:        https://github.com/calamares/calamares/releases/download/v%{version}/calamares-%{version}.tar.gz
Source1:        settings.conf
Source2:        branding.desc


BuildRequires:  git-core
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.245
BuildRequires:  gcc-c++ >= 9.0.0
BuildRequires:  pkgconfig
BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  polkit-qt6-1-devel

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(KPMcore) >= 4.2.0
BuildRequires:  python3-devel >= 3.3
BuildRequires:  python3-jsonschema
BuildRequires:  python3-pyyaml
BuildRequires:  boost-devel >= 1.55.0
%global __python %{__python3}
BuildRequires:  cmake(AppStreamQt) >= 1.0.0
BuildRequires:  libpwquality-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  parted-devel
BuildRequires:  yaml-cpp-devel >= 0.5.1

Requires:       system-logos
Requires:       coreutils
Requires:       util-linux
Requires:       upower
Requires:       NetworkManager
Requires:       dracut
Requires:       grub2
Requires:       efibootmgr
Requires:       console-setup
Requires:       setxkbmap
Requires:       os-prober
Requires:       e2fsprogs
Requires:       dosfstools
Requires:       ntfsprogs
Requires:       gawk
Requires:       systemd
Requires:       rsync
Requires:       shadow-utils
Requires:       dnf
Requires:       kdesu
Requires:       hicolor-icon-theme

%description
Calamares is a distribution-independent installer framework.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake_kf6 -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
             -DBUILD_TESTING:BOOL=OFF \
             -DWITH_PYBIND11:BOOL=OFF \
             -DWITH_QT6:BOOL=ON \
             %{nil}
%cmake_build

%install
%cmake_install

# Install custom settings
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/calamares/settings.conf

# Install custom branding
mkdir -p %{buildroot}%{_datadir}/calamares/branding/default
install -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/calamares/branding/default/branding.desc


%files
%{_bindir}/calamares
%{_datadir}/calamares
%{_datadir}/applications/calamares.desktop
# Calamares installed files we missed
%{_libdir}/calamares/
%{_libdir}/libcalamares.so*
%{_datadir}/icons/hicolor/*/apps/calamares.svg
%{_mandir}/man8/calamares.8*
%{_datadir}/polkit-1/actions/com.github.calamares.calamares.policy
# Settings
%config(noreplace) %{_sysconfdir}/calamares/settings.conf
%exclude %{_includedir}
# We can include branding here or above
%dir %{_sysconfdir}/calamares/
%dir %{_datadir}/calamares/branding

