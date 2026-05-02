import dns.resolver

def dns_lookup(domain: str) -> list:
    try:
        answers = dns.resolver.resolve(domain, "A")
        return [rdata.to_text() for rdata in answers]
    except Exception:
        return []
