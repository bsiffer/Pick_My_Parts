from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    home_content = """
    <p>This is home page for our app!</p>
    """
    return render(request, 'core/base_template.html', { 'custom_html' : home_content})

def about(request):
    about_content = """
    <b>Pick My Parts</b>
    <br/>
    <i>v 0.0.1</i>
    <br/><br/>
    <p>
        <span>
            <b>Developers</b>
            <ol>
                <li>Anurodh Patrekar</li>
                <li>Brandon Siffer</li>
                <li>Corey Devolld</li>
                <li>Devin Hackman</li>
                <li>Jerilyn Lopez</li>
                <li>Michael Angelo Stainback</li>
                <li>Reena Shrestha</li>
            </ol>
        </span>
    </p>
    """
    return render(request, 'core/base_template.html', { 'custom_html' : about_content })

def cpus(request):
    page_content = """
        <h1>All CPUs available</h1>
        """
    return render(request, 'core/base_template.html', {'custom_html': page_content})

def under_construction(request):
    page_content = """
        <b>Under Construction!</b><br/>
        <i>This page will be available soon.</i>
        """
    return render(request, 'core/base_template.html', {'custom_html': page_content})
