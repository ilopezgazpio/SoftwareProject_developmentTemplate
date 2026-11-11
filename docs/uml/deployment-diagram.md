# Deployment diagram

*Where the software runs, and which external services and endpoints it depends on. There is no server and no GPU: everything runs on a laptop and talks to services we do not operate.*

```mermaid
flowchart TB
    subgraph LAPTOP["«device» Student laptop"]
        PY["«execution environment» Python 3.12"]
        PKG["«artifact» lmeval package"]
        ENV["«artifact» .env<br/>LMEVAL_PROVIDER, LATXA_API_KEY, LATXA_API_URL"]
        D["data/ · EusTrivia JSONL<br/>(ignored by Git)"]
        R["runs/ · saved runs<br/>(ignored by Git)"]
        F["tests/fixtures/ · recorded Latxa answers<br/>(committed)"]
        PY --- PKG
        PKG --- ENV
        PKG --- D
        PKG --- R
        PKG --- F
    end

    subgraph HITZ["«node» HiTZ servers"]
        API["«service» Latxa text API<br/>endpoint: address sent with the key<br/>HTTPS · JSON · Bearer key · 40 req/min · HTTP 429 above"]
    end

    subgraph GH["«node» GitHub"]
        REPO["repository · issues · project board<br/>(Actions from the midterm sprint)"]
    end

    subgraph EGELA["«node» eGela"]
        DL["EusTrivia sample · recorded answers"]
    end

    PKG -->|"HTTPS, only with LMEVAL_PROVIDER=latxa"| API
    LAPTOP <-->|"git push / pull"| REPO
    DL -->|"manual download, once"| D
    DL -->|"manual download, once"| F
```

## Notes

- **Offline path.** With `LMEVAL_PROVIDER=replay` nothing leaves the laptop. This is how tests run and how the demonstration is given.
- **Live path.** With `LMEVAL_PROVIDER=latxa` the package calls the Latxa endpoint. The address and the key come from HiTZ with the key request, from 17 November, and live only in `.env`.
- **No other endpoint.** P2 does not use the CLARIAH-EUS OCR or speech services.
