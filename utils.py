def is_instagram_link(link: str):
    # Checking domain instagram
    instagram_domains = ['instagram.com','www.instagram.com']

    return any(domain in link for domain in instagram_domains)
