from pathlib import Path

from nfelib.nfe.client.v4_0.servers_scraper import main

OUTPUT_FILE = Path("nfelib/nfe/client/v4_0/servers.py")


def read_current_servers():
    return OUTPUT_FILE.read_text(encoding="utf-8") if OUTPUT_FILE.exists() else ""


def test_scraper():
    old_content = read_current_servers()
    main()
    new_content = read_current_servers()
    assert new_content == old_content, (
        "Server list has changed. Review and commit the new file."
    )
