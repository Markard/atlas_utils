import logging
import os
from logging import Logger

from atlassian import Confluence

from export_pdf.entities.hierarchy import Hierarchy
from export_pdf.entities.page import Page


class PdfExporter:
    confluence: Confluence
    logger: Logger

    def __init__(self, confluence: Confluence):
        self.confluence = confluence

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(f"{__name__}.log", mode='w')
        handler.setFormatter(logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s"))
        logger.addHandler(handler)

        self.logger = logger

    def export(self, space_key: str, export_dir: str):
        hierarchy = self.__get_page_hierarchy(space_key)
        for page_id in hierarchy.pages:
            self.__export_page(export_dir, hierarchy.pages[page_id])

    def __get_page_hierarchy(self, space_key: str) -> Hierarchy:
        pages = self.confluence.get_all_pages_from_space(space_key)
        hierarchy = Hierarchy()

        for page in pages:
            page_id = page['id']
            details = self.confluence.get_page_by_id(page_id, expand='ancestors')
            ancestors = [ancestor['title'] for ancestor in details['ancestors']]
            title = details['title']

            hierarchy.add_page(Page(page_id, title, ancestors))
        return hierarchy

    def __export_page(self, export_dir: str, page: Page) -> None:
        try:
            dir_path = os.path.join(export_dir, page.path)
            os.makedirs(dir_path, exist_ok=True)

            pdf_content = self.confluence.export_page(page.id)
            filename = f"{page.title}.pdf"
            file_path = os.path.join(dir_path, filename)

            with open(file_path, 'wb') as f:
                f.write(pdf_content)

            self.logger.info(f"Страница сохранена: {file_path}")

        except Exception as e:
            self.logger.error(f"Ошибка при экспорте {page.id}: {str(e)}")
