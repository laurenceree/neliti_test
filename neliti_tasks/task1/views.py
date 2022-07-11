from genericpath import exists
from multiprocessing.dummy import active_children
from django.shortcuts import render
from django.http import HttpResponse
from .models import Journal, Publication, Hit
import json

def index(request):
    return HttpResponse(json.dumps(get_journal_statistics()))

def get_journal_statistics():
    # Construct summary dict in the form {journal_id -> (total_views, total_downloads)}
    # Declare empty dictionary 
    summary = dict()
    
    # Get all Journals
    journals = Journal.objects.all()
    
    # Get all Publications
    pubs = Publication.objects.all()

    # Get all Hits
    hits = Hit.objects.all()

    # Caculate pageviews and downloads of all journals
    for journal in journals:
        # Initialize with (0, 0)
        summary[journal.id] = (0, 0)

        # Get all publication ids of this journal
        pub_ids = pubs.filter(journal_id=journal.id).values_list('id', flat=True)

        # Get all hits of this journal
        hits_of_journal = hits.filter(publication_id__in=pub_ids)

        # Get number of PAGEVIEW hits
        pageviews = hits_of_journal.filter(action=Hit.PAGEVIEW).count()
        
        # Get number of DOWNLOAD hits
        downloads = hits_of_journal.filter(action=Hit.DOWNLOAD).count()
        
        # Assign pageviews and downloads
        summary[journal.id] = (pageviews, downloads)   
    
    return summary
    

