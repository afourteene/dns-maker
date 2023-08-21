zone = """
;
; BIND data file for local loopback interface
;
$TTL	604800
@	IN	SOA	{domain}. root.{domain}. (
			      2		; Serial
			   4800		; Refresh
			   6400		; Retry
			2419200		; Expire
			    800 )	; Negative Cache TTL
;
	NS	{ns1}.
	NS	{ns2}.
www	A	{ip}
w	CNAME	{domain}.
ww	CNAME	{domain}.

"""



reverseZone = """
;
; BIND data file for local loopback interface
;
$TTL	604800
@	IN	SOA	{revIp}.in-addr.arpa. root.your-domain (
			      2		; Serial
			    4800	; Refresh
			  86400		; Retry
			2419200		; Expire
			    4800 )	; Negative Cache TTL
;
	NS	{ns1}.
	NS	{ns2}.
{lastIpPart}	PTR	{domain}.

"""