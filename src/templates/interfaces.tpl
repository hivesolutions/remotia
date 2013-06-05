# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo eth0
iface lo inet loopback

# The primary network interface
iface eth0 inet static
        address {{ net.ip_address }}
        netmask {{ net.netmask }}
        broadcast {{ net.broadcast }}
        network {{ net.network }}
        dns-nameservers {% for dns_server in net.dns_servers %}{{ dns_server }} {% endfor %}
        dns-search {{ net.domain }}
        dns-domain {{ net.domain }}
        gateway {{ net.gateway }}
