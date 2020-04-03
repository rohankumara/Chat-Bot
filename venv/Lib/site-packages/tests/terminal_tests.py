from ChatTerminal import Session


class TestTerminal(object):
    test_host_ip = "118.126.111.64"
    chat_session = Session(test_host_ip)

    def test_ls(self):
        self.chat_session.execute("ls")
        self.chat_session.close()
