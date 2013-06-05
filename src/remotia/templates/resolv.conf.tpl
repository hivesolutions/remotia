{% for dns_server in net.dns_servers %}
nameserver {{ dns_server }}{% endfor %}
domain {{ net.domain }}
