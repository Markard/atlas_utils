from export_pdf.entities.page import Page


class Hierarchy:
    pages: dict = {}

    def add_page(self, page: Page):
        self.pages[page.id] = page
