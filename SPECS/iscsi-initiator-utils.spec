%define open_iscsi_version	2.0
%define open_iscsi_build	873

Summary: iSCSI daemon and utility programs
Name: iscsi-initiator-utils
Version: 6.%{open_iscsi_version}.%{open_iscsi_build}
Release: 16%{?dist}
Group: System Environment/Daemons
License: GPLv2+
URL: http://www.open-iscsi.org

Source0: http://www.open-iscsi.org/bits/open-iscsi-%{open_iscsi_version}-%{open_iscsi_build}.tar.gz
Source4: 04-iscsi
Source5: iscsi-tmpfiles.conf

# upstream patches, post last tagged version
Patch1: 0001-iscsid-fix-iscsid-segfault-during-qla4xxx-login.patch
Patch2: 0002-ISCSISTART-Bring-up-the-corresponding-network-interf.patch
Patch3: 0003-iscsi-tools-fix-compile-error-when-OFFLOAD_BOOT_SUPP.patch
Patch4: 0004-ISCSID-Passing-more-net-params-from-ibft-to-iface.patch
Patch5: 0005-iscsi-tools-Convert-r-argument-to-an-integer-before-.patch
Patch6: 0006-Update-README-for-removal-of-DBM-requirement.patch
Patch7: 0007-iscsid-iscsiadm-fix-abstract-socket-length-in-bind-c.patch
Patch8: 0008-iscsid-implement-systemd-compatible-socket-activatio.patch
Patch9: 0009-iscsid-add-example-unit-files-for-systemd.patch
Patch10: 0010-iscsi-tools-fix-get_random_bytes-error-handling.patch
Patch11: 0011-ISCSID-Added-socket-communication-hooks-for-uip.patch
Patch12: 0012-ISCSID-Modified-the-Makefile-for-iscsiuio-compilatio.patch
Patch13: 0013-ISCSID-Added-iscsiuio-source-to-the-open-iscsi-pkg.patch
Patch14: 0014-From-Adheer-Chandravanshi-adheer.chandravanshi-qlogi.patch
Patch15: 0015-Manpage-changes-for-flashnode-submode-support-for-ho.patch
Patch16: 0016-README-changes-for-flashnode-submode-support-for-hos.patch
Patch17: 0017-PATCH-1-of-1-correctly-check-return-value-of-nice.patch
Patch18: 0018-Allow-firmware-mode-to-use-debug-flag.patch
Patch19: 0019-iscsiadm-return-error-when-login-fails.patch
Patch20: 0020-iscsiadm-bind-ifaces-to-portals-found-using-isns.patch
Patch21: 0021-iscsiadm-Check-for-mode-is-not-required-when-creatin.patch
Patch22: 0022-iscsid-iscsiadm-add-support-for-emulex-one-connect-s.patch
Patch23: 0023-ISCSIUIO-Updated-iscsiuio-to-version-0.7.8.1b-for-pe.patch
Patch24: 0024-Fix-discovery-error-return-without-return-value.patch
Patch25: 0025-iscsid-Fix-strlen-parameter.patch
Patch26: 0026-iscsiuio-Change-socket-bind-to-use-the-same-struct-s.patch
Patch27: 0027-Make-rescan-run-in-parallel.patch
# not (yet) upstream merged
Patch40: 0040-ISCSISTART-Saved-ibft-boot-info-to-the-session-sysfs.patch
Patch41: 0041-ISCSID-Added-the-extraction-of-the-session-boot-info.patch
Patch42: 0042-ISCSID-Added-iface-content-override-fix.patch
Patch43: 0043-idmb_rec_write-check-for-tpgt-first.patch
Patch45: 0045-idbm_rec_write-seperate-old-and-new-style-writes.patch
Patch46: 0046-idbw_rec_write-pick-tpgt-from-existing-record.patch
Patch47: 0047-iscsiuio-systemd-socket-activation-support.patch
Patch49: 0049-update-systemd-service-files-add-iscsi.service-for-s.patch
Patch50: 0050-iscsi-boot-related-service-file-updates.patch
# distro specific modifications
Patch51: 0051-update-initscripts-and-docs.patch
Patch52: 0052-use-var-for-config.patch
Patch53: 0053-use-red-hat-for-name.patch
Patch54: 0054-add-libiscsi.patch
Patch55: 0055-dont-use-static.patch
Patch56: 0056-remove-the-offload-boot-supported-ifdef.patch
Patch59: 0059-iscsiuio-systemd-unit-files.patch
Patch60: 0060-use-systemctl-to-start-iscsid.patch
Patch61: 0061-resolve-565245-multilib-issues-caused-by-doxygen.patch
Patch62: 0062-Don-t-check-for-autostart-sessions-if-iscsi-is-not-u.patch
Patch63: 0063-fix-order-of-setting-uid-gid-and-drop-supplementary-.patch
Patch64: 0064-libiscsi-fix-incorrect-strncpy-use.patch
Patch65: 0065-fix-hardened-build-of-iscsiuio.patch
Patch66: 0066-start-socket-listeners-on-iscsiadm-command.patch
# version string, needs to be updated with each build
Patch99: 0099-use-Red-Hat-version-string-to-match-RPM-package-vers.patch

BuildRequires: flex bison python-devel doxygen kmod-devel systemd-devel
# For dir ownership
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%global _hardened_build 1
%global __provides_exclude_from ^(%{python_sitearch}/.*\\.so)$

%description
The iscsi package provides the server daemon for the iSCSI protocol,
as well as the utility programs used to manage it. iSCSI is a protocol
for distributed disk access using SCSI commands sent over Internet
Protocol networks.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n open-iscsi-%{open_iscsi_version}-%{open_iscsi_build}
# upstream patches
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
# pending upstream merge
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch49 -p1
%patch50 -p1
# distro specific modifications
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
# version string
%patch99 -p1

# change exec_prefix, there's no easy way to override
%{__sed} -i -e 's|^exec_prefix = /$|exec_prefix = %{_exec_prefix}|' Makefile

%build

# configure sub-packages from here
# letting the top level Makefile do it will lose setting from rpm
cd iscsiuio
%{__chmod} +x configure
%{configure}
cd ..
cd utils/open-isns
%{configure}
cd ../..

%{__make} OPTFLAGS="%{optflags} %{?__global_ldflags} -DUSE_KMOD -lkmod"
pushd libiscsi
python setup.py build
touch -r libiscsi.doxy html/*
popd


%install
%{__make} DESTDIR=%{?buildroot} install_programs install_doc install_etc
# upstream makefile doesn't get everything the way we like it
rm $RPM_BUILD_ROOT%{_sbindir}/iscsi_discovery
rm $RPM_BUILD_ROOT%{_mandir}/man8/iscsi_discovery.8
%{__install} -pm 755 usr/iscsistart $RPM_BUILD_ROOT%{_sbindir}
%{__install} -pm 644 doc/iscsistart.8 $RPM_BUILD_ROOT%{_mandir}/man8
%{__install} -pm 644 doc/iscsi-iname.8 $RPM_BUILD_ROOT%{_mandir}/man8
%{__install} -d $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
%{__install} -pm 644 iscsiuio/iscsiuiolog $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d

%{__install} -d $RPM_BUILD_ROOT%{_sharedstatedir}/iscsi
%{__install} -d $RPM_BUILD_ROOT%{_sharedstatedir}/iscsi/nodes
%{__install} -d $RPM_BUILD_ROOT%{_sharedstatedir}/iscsi/send_targets
%{__install} -d $RPM_BUILD_ROOT%{_sharedstatedir}/iscsi/static
%{__install} -d $RPM_BUILD_ROOT%{_sharedstatedir}/iscsi/isns
%{__install} -d $RPM_BUILD_ROOT%{_sharedstatedir}/iscsi/slp
%{__install} -d $RPM_BUILD_ROOT%{_sharedstatedir}/iscsi/ifaces

# for %%ghost
%{__install} -d $RPM_BUILD_ROOT/var/lock/iscsi
touch $RPM_BUILD_ROOT/var/lock/iscsi/lock


%{__install} -d $RPM_BUILD_ROOT%{_unitdir}
%{__install} -pm 644 etc/systemd/iscsi.service $RPM_BUILD_ROOT%{_unitdir}
%{__install} -pm 644 etc/systemd/iscsid.service $RPM_BUILD_ROOT%{_unitdir}
%{__install} -pm 644 etc/systemd/iscsid.socket $RPM_BUILD_ROOT%{_unitdir}
%{__install} -pm 644 etc/systemd/iscsiuio.service $RPM_BUILD_ROOT%{_unitdir}
%{__install} -pm 644 etc/systemd/iscsiuio.socket $RPM_BUILD_ROOT%{_unitdir}

%{__install} -d $RPM_BUILD_ROOT%{_libexecdir}
%{__install} -pm 755 etc/systemd/iscsi-mark-root-nodes $RPM_BUILD_ROOT%{_libexecdir}

%{__install} -d $RPM_BUILD_ROOT%{_sysconfdir}/NetworkManager/dispatcher.d
%{__install} -pm 755 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/NetworkManager/dispatcher.d

%{__install} -d $RPM_BUILD_ROOT%{_tmpfilesdir}
%{__install} -pm 644 %{SOURCE5} $RPM_BUILD_ROOT%{_tmpfilesdir}/iscsi.conf

%{__install} -d $RPM_BUILD_ROOT%{_libdir}
%{__install} -pm 755 libiscsi/libiscsi.so.0 $RPM_BUILD_ROOT%{_libdir}
%{__ln_s}    libiscsi.so.0 $RPM_BUILD_ROOT%{_libdir}/libiscsi.so
%{__install} -d $RPM_BUILD_ROOT%{_includedir}
%{__install} -pm 644 libiscsi/libiscsi.h $RPM_BUILD_ROOT%{_includedir}

%{__install} -d $RPM_BUILD_ROOT%{python_sitearch}
%{__install} -pm 755 libiscsi/build/lib.linux-*/libiscsimodule.so \
	$RPM_BUILD_ROOT%{python_sitearch}


%post
/sbin/ldconfig

%systemd_post iscsi.service iscsid.service iscsiuio.service iscsid.socket iscsiuio.socket

if [ $1 -eq 1 ]; then
	if [ ! -f %{_sysconfdir}/iscsi/initiatorname.iscsi ]; then
		echo "InitiatorName=`/usr/sbin/iscsi-iname`" > %{_sysconfdir}/iscsi/initiatorname.iscsi
	fi
	# enable socket activation and persistant session startup by default
	/bin/systemctl enable iscsi.service >/dev/null 2>&1 || :
	/bin/systemctl enable iscsid.socket >/dev/null 2>&1 || :
	/bin/systemctl enable iscsiuio.socket >/dev/null 2>&1 || :
fi

%preun
%systemd_preun iscsi.service iscsid.service iscsiuio.service iscsid.socket iscsiuio.socket

%postun
/sbin/ldconfig
%systemd_postun

%triggerun -- iscsi-initiator-utils < 6.2.0.873-1
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply iscsid
# and systemd-sysv-convert --apply iscsi
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save iscsi >/dev/null 2>&1 ||:
/usr/bin/systemd-sysv-convert --save iscsid >/dev/null 2>&1 ||:

# enable socket activation
/bin/systemctl enable iscsid.socket >/dev/null 2>&1 || :
/bin/systemctl enable iscsiuio.socket >/dev/null 2>&1 || :

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del iscsid >/dev/null 2>&1 || :
/sbin/chkconfig --del iscsi >/dev/null 2>&1 || :
/bin/systemctl try-restart iscsid.service >/dev/null 2>&1 || :
/bin/systemctl try-restart iscsi.service >/dev/null 1>&1 || :

%files
%doc README
%dir %{_sharedstatedir}/iscsi
%dir %{_sharedstatedir}/iscsi/nodes
%dir %{_sharedstatedir}/iscsi/isns
%dir %{_sharedstatedir}/iscsi/static
%dir %{_sharedstatedir}/iscsi/slp
%dir %{_sharedstatedir}/iscsi/ifaces
%dir %{_sharedstatedir}/iscsi/send_targets
%ghost %{_var}/lock/iscsi
%ghost %{_var}/lock/iscsi/lock
%{_unitdir}/iscsi.service
%{_unitdir}/iscsid.service
%{_unitdir}/iscsid.socket
%{_unitdir}/iscsiuio.service
%{_unitdir}/iscsiuio.socket
%{_libexecdir}/iscsi-mark-root-nodes
%{_sysconfdir}/NetworkManager/dispatcher.d/04-iscsi
%{_tmpfilesdir}/iscsi.conf
%dir %{_sysconfdir}/iscsi
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/iscsi/iscsid.conf
%{_sbindir}/*
%{_libdir}/libiscsi.so.0
%{python_sitearch}/libiscsimodule.so
%{_mandir}/man8/*
%config(noreplace) %{_sysconfdir}/logrotate.d/iscsiuiolog

%files devel
%doc libiscsi/html
%{_libdir}/libiscsi.so
%{_includedir}/libiscsi.h

%changelog
* Mon Nov 25 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-16
- fix iscsiuio socket activation
- have systemd start socket units on iscsiadm use, if not already listening

* Sun Sep 15 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-15
- move /sbin to /usr/sbin
- use rpm macros in install rules

* Fri Sep 13 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-14
- fix iscsiuio hardened build and other compiler flags

* Fri Aug 23 2013 Andy Grover <agrover@redhat.com> - 6.2.0.873-13
- Fix patch 0041 to check session != NULL before calling iscsi_sysfs_read_boot()

* Tue Aug 20 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-12
- fix regression in last build, database records can't be accessed

* Mon Aug 19 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-11
- iscsi boot related fixes
  make sure iscsid gets started if there are any boot sessions running
  add reload target to fix double session problem when restarting from NM
  don't rely on session list passed from initrd, never got fully implemented
  remove patches related to running iscsid from initrd, possible to revisit later

* Sun Aug 18 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-10
- sync with upstream git, minor context fixes after rebase of out-of-tree patches
- iscsiuio is merged upstream, remove old source archive and patches
- spec cleanups to fix rpmlint issues

* Sun Aug  4 2013 Peter Robinson <pbrobinson@fedoraproject.org> 6.2.0.873-9
- Fix FTBFS, cleanup spec

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0.873-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-7
- Use the systemd tmpfiles service to recreate lockfiles in /var/lock
- 955167 build as a position independent executable
- 894576 fix order of setuid/setgid and drop additional groups

* Tue May 28 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-6
- Don't have iscsiadm scan for autostart record if node db is empty (bug #951951)

* Tue Apr 30 2013 Orion Poplawski <orion@cora.nwra.com> - 6.2.0.873-5
- Fix typo in NM dispatcher script (bug #917058)

* Thu Feb 21 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-4
- build with libkmod support, instead of calling out to modprobe
- enable socket activation by default

* Thu Jan 24 2013 Kalev Lember <kalevlember@gmail.com> - 6.2.0.873-3
- Fix the postun script to not use ldconfig as the interpreter

* Wed Jan 23 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-2
- package iscsi_mark_root_nodes script, it's being referenced by the unit files

* Tue Jan 22 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-1
- rebase to new upstream code
- systemd conversion
- 565245 Fix multilib issues caused by timestamp in doxygen footers

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0.872-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 14 2012 Mike Christie <mchristi@redhat.com> 6.2.0.872.18
- 789683 Fix boot slow down when the iscsi service is started
  (regression added in 6.2.0.872.16 when the nm wait was added).

* Mon Feb 6 2012 Mike Christie <mchristi@redhat.com> 6.2.0.872.17
- 786174 Change iscsid/iscsi service startup, so it always starts
  when called.

* Sat Feb 4 2012 Mike Christie <mchristi@redhat.com> 6.2.0.872.16
- 747479 Fix iscsidevs handling of network requirement

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0.872-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.14
- Fix version string to reflect fedora and not rhel.

* Tue Oct 18 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.13
- Update iscsi tools.

* Sat Apr 30 2011 Hans de Goede <hdegoede@redhat.com> - 6.2.0.872-12
- Change iscsi init scripts to check for networking being actually up, rather
  then for NetworkManager being started (#692230)

* Tue Apr 26 2011 Hans de Goede <hdegoede@redhat.com> - 6.2.0.872-11
- Fix iscsid autostarting when upgrading from an older version
  (add iscsid.startup key to iscsid.conf on upgrade)
- Fix printing of [ OK ] when successfully stopping iscsid
- systemd related fixes:
 - Add Should-Start/Stop tgtd to iscsi init script to fix (re)boot from
   hanging when using locally hosted targets
 - %%ghost /var/lock/iscsi and contents (#656605)

* Mon Apr 25 2011 Mike Christie <mchristi@redhat.com> 6.2.0.872-10
- Fix iscsi init scripts check for networking being up (#692230)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0.872-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
