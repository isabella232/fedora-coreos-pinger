# Generated by rust2rpm-9-1.fc30
%bcond_without check

%global crate fedora-coreos-metrics-client

Name:           rust-%{crate}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Metrics collection client for Fedora CoreOS

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/fedora-coreos-metrics-client
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(failure/default) >= 0.1.5 with crate(failure/default) < 0.2.0)
BuildRequires:  (crate(glob/default) >= 0.3.0 with crate(glob/default) < 0.4.0)
BuildRequires:  (crate(log/default) >= 0.4.6 with crate(log/default) < 0.5.0)
BuildRequires:  (crate(serde/default) >= 1.0.91 with crate(serde/default) < 2.0.0)
BuildRequires:  (crate(serde/derive) >= 1.0.91 with crate(serde/derive) < 2.0.0)
BuildRequires:  (crate(toml/default) >= 0.5.1 with crate(toml/default) < 0.6.0)

%global _description \
Metrics collection client for Fedora CoreOS

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/%{crate}
%{_unitdir}/%{crate}.service
%dir %{_sysconfdir}/%{crate}
%dir /run/%{crate}
%dir %{_prefix}/lib/%{crate}
%{_prefix}/lib/%{crate}/config.d/0000-client-default.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install
%{__install} -Dpm0644 -t %{buildroot}%{_unitdir} \
  dist/systemd/*.service
%{__mkdir_p} %{buildroot}%{_sysconfdir}/%{crate}
%{__mkdir_p} %{buildroot}/run/%{crate}
%{__mkdir_p} %{buildroot}%{_prefix}/lib/%{crate}
%{__install} -Dpm0644 -t %{buildroot}%{_prefix}/lib/config.d/%{crate} \
  dist/0000-client-default.toml

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Tue May 28 04:36:46 UTC 2019 Robert Fairley <rfairley@redhat.com> - 0.1.0-1
- Initial package
