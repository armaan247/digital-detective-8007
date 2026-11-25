# Mission 07 — How Computers Communicate

---

## 1. Mission Title

**Mission 07: How Computers Communicate**

---

## 2. Task / Objective

Explain foundational networking concepts (`LAN`, `MAN`, `WAN`, `DNS`, `Router`, `Protocol`, `Packet switching`, `Client-server`), test connectivity and DNS resolution safely in Terminal, and trace step by step what happens when a website opens in a browser.

---

## 3. Work Completed

### Task 7.1 — Explain Network Concepts

| Concept | Explain It in Your Own Words | Example |
|---------|------------------------------|---------|
| **LAN** | A Local Area Network connects computers and devices within a small physical space, such as a home, classroom, or office. | Laptops, printers, and phones connected to a home or lab Wi-Fi router. |
| **MAN** | A Metropolitan Area Network spans a larger area than a LAN, typically linking multiple buildings across a university campus or city. | Connected networks linking different academic buildings across a college campus. |
| **WAN** | A Wide Area Network connects networks across cities, countries, or continents over long distances. | The global internet, or a company network connecting offices in different cities. |
| **DNS** | The Domain Name System works like a phonebook for the internet, translating human-readable domain names into numeric IP addresses. | Translating `example.com` into `104.20.23.154` and `172.66.147.243`. |
| **Router** | A networking device that joins different networks together and chooses the best path to forward data packets between them. | A home Wi-Fi router connecting devices on the local LAN to the ISP's external network. |
| **Protocol** | An agreed-upon set of rules and formats that devices follow so they can communicate reliably. | `HTTPS` for encrypted web pages, `DNS` for name lookups, and `ICMP` used by `ping`. |
| **Packet switching** | Instead of sending a whole file in one piece, data is split into small packets that travel across shared network links and are reassembled at the destination. | A web page's HTML and images broken into IP packets routed across the internet and put back together by the browser. |
| **Client-server** | A communication model where a client program sends a request for data or a service, and a server processes the request and sends back a response. | A web browser (client) requesting a page from the web server hosting `example.com`. |

---

### Task 7.2 — Observe Network Information

I ran safe connectivity and DNS lookup tests for the public domain `example.com` from Terminal. All local network identifiers (my own IP address and the local DNS resolver IP) were redacted.

#### Observations

- **Connectivity test (`ping -c 4 example.com`):**
  Sent `4` ICMP echo packets to `example.com` (`104.20.23.154`), and all `4` replies came back (`0.0% packet loss`), with round-trip times between `25.497 ms` and `33.858 ms` (average `31.088 ms`).
- **DNS lookup (`nslookup example.com`):**
  Queried the local DNS server (`[redacted]`, port `53`) and received the public IPv4 addresses associated with `example.com`: `172.66.147.243` and `104.20.23.154`.

#### Answers to Questions

- **What does a connectivity test help you check?**
  A connectivity test like `ping` checks whether your computer can reach a destination host over the network, whether packets are getting dropped (`packet loss`), and how long a round trip takes (latency in milliseconds).
- **What information does a DNS lookup display?**
  `nslookup` displays the DNS server that answered the query (redacted here for privacy) along with the domain name and the IP address(es) mapped to that domain.
- **What is the role of DNS when you enter a website name in a browser?**
  Because network routers deliver packets using numeric IP addresses rather than English domain names, DNS translates the website name you type (such as `example.com`) into the server's IP address before the browser can connect.

---

### Task 7.3 — What Happens When You Open a Website?

1. **User enters the address in the client:** You type a website URL (like `https://example.com`) into your web browser, which acts as the **client**.
2. **DNS lookup:** The browser checks if it already knows the address; if not, your OS sends a **DNS** query through your local network to find the **server**'s IP address (for example, `104.20.23.154`).
3. **Routing over the network:** Using that IP address, your device sends connection packets through your local router and across intermediate routers on the ISP/internet toward the destination network.
4. **Protocol handshake and request:** The client and **server** follow standard network rules (**protocols** such as TCP, TLS, and HTTP/HTTPS) to set up a secure connection, and the browser sends an HTTP/HTTPS `GET` request for the page.
5. **Server processes the request:** The web **server** receives the request, prepares the requested webpage content (HTML, CSS, status code like `200 OK`), and sends it back as packets across the network.
6. **Browser displays the response:** Your **client** browser receives and reassembles the packets, interprets the HTML/CSS, and renders the finished webpage on your screen.

---

## 4. Commands / Tools Used

| Command / Tool | Purpose |
|----------------|---------|
| `ping -c 4 example.com` | Sent 4 test packets to `example.com` to verify reachability, packet loss, and round-trip latency |
| `nslookup example.com` | Queried DNS to observe the IP addresses mapped to `example.com` |

---

## 5. My Understanding

- Networks scale from local setups (LAN) to campus/city networks (MAN) and global connections (WAN), linked together by routers forwarding packets.
- Tools like `ping` and `nslookup` let us test two separate layers quickly: `nslookup` checks whether domain-to-IP translation works, while `ping` checks whether packets can travel to that host and return.
- Opening any website depends on the client-server model, DNS name resolution, packet switching, and shared protocols working in order.

---

## 6. Difficulties Faced

- The raw `nslookup` output displayed the private IP address of the local DNS server (`Server:` and `Address:`), which had to be spotted and redacted before saving any files.

---

## 7. How I Resolved Them

- I reviewed the `ping` and `nslookup` output line by line and replaced the local DNS resolver IP address with `[redacted]` in both [`evidence/mission-07-network-output.txt`](../evidence/mission-07-network-output.txt) and this README.

---

## 8. Evidence / Files

| Evidence Item | Description |
|---------------|-------------|
| [Mission 07 README](README.md) | Network concepts table, connectivity/DNS notes, and 6-step website loading trace |
| [Mission 07 network output](../evidence/mission-07-network-output.txt) | Privacy-safe copy of `ping -c 4 example.com` and `nslookup example.com` outputs |

---

## 9. Commit Details

- Commit message: `Explain networking concepts and website communication`
- Commit hash: `e858aa9`
- Branch: `main`
- Status: Pushed to `origin/main` and verified.
