
from django.core.management.base import BaseCommand
from chatbot.rag.vector_store import build_vector_store

class Command(BaseCommand):
    help = 'Rebuilds the RAG vector store.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to rebuild the RAG vector store...'))
        build_vector_store()
        self.stdout.write(self.style.SUCCESS('Successfully rebuilt the RAG vector store.'))
