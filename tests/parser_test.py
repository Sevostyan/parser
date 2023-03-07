from main import PDFparser, HTMLParser, DOCParser, DOCXparser


class TestPDFParser:
    def test_text(self):
        parser = PDFparser()
        data = parser.parse('./data/test_retrival.pdf')
        gt = ["Testing retrival",
              "Egor Razumilov, Danila Sevostyanov, Egor Ershov",
              "March 2023",
              "1",
              "Introduction",
              "loren ipsum, loren ipsun",
              "1"]
        assert len(data) == len(gt)
        for i in range(len(data)):
            assert data[i] == gt[i]

class TestDOCXParser:
    def test_text(self):
        parser = DOCXparser()
        data = parser.parse('./data/test_retrival.docx')
        gt = ['TEST Retrival',
              'Egor Razumilov, Danila Sevostyanov, Egor Ershov',
              'Loren ipsum, LOREN IPSUM']
        assert len(data) == len(gt)
        for i in range(len(data)):
            assert data[i] == gt[i]

class TestDOCparser:
    def test_text(self):
        parser = DOCParser()
        data = parser.parse('./data/test_retrival.docx')
        gt = ['TEST Retrival',
              'Egor Razumilov, Danila Sevostyanov, Egor Ershov',
              'Loren ipsum, LOREN IPSUM']
        assert len(data) == len(gt)
        for i in range(len(data)):
            assert data[i] == gt[i]

class TestHTMLparser:
    def test(self):
        parser = HTMLParser()
        text = """
        <html>
        <head>
          <title>Head's title</title>
        </head>
        
        <body>
          <p class="title"><b>Body's title</b></p>
          <p class="story">line begins
            <a href="http://example.com/element1" class="element" id="link1">1</a>
            <a href="http://example.com/element2" class="element" id="link2">2</a>
            <a href="http://example.com/avatar1" class="avatar" id="link3">3</a>
          <p> line ends</p>
        </body>
        </html>
        """
        data = parser.parse(text)
        assert data.head.get_text().strip() == "Head's title"
        assert data.body.p.get_text().strip() == "Body's title"