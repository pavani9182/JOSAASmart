from django.shortcuts import render
from .models import josaa
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
from django.db.models import Q


def home(request):
    return render(request, 'home.html')
def Institute_analysis(request):
    Institute = request.GET.get('Institute')
    Seat_Type =request.GET.get('Seat_Type')
    Gender = request.GET.get('Gender')
    year = request.GET.get('year')
    round = request.GET.get('round')
    

    In_data = josaa.objects.filter(
        Institute=Institute,
        Seat_Type=Seat_Type,
        Gender=Gender,
        year=year,
        round=round,
        )
    
    

    context = {
        'In_data': In_data
    }

    return render(request, 'Institute_analysis.html', context)

def Branch_analysis(request):
    
    Academic_Program_Name = request.GET.get('Academic_Program_Name')
    Seat_Type =request.GET.get('Seat_Type')
    Gender = request.GET.get('Gender')
    year = request.GET.get('year')
    round = request.GET.get('round')
    

    br_data = josaa.objects.filter(
        Academic_Program_Name=Academic_Program_Name,
        Seat_Type=Seat_Type,
        Gender=Gender,
        year=year,
        round=round,
        )
    
    context = {
        'br_data': br_data
    }

    return render(request, 'branch_analysis.html', context)

   

def trendsoveryears(request):

    Academic_Program_Name = request.GET.get('Academic_Program_Name')
    Institute = request.GET.get('Institute')
    Seat_Type = request.GET.get('Seat_Type')
    Gender = request.GET.get('Gender')
    round = request.GET.get('round')
    
    tr_data = josaa.objects.filter(
        Academic_Program_Name=Academic_Program_Name,
        Institute=Institute,
        Seat_Type=Seat_Type,
        Gender=Gender,
        round=round,
    )

    # Convert queryset to a DataFrame
    data = {
        'Year': [entry.year for entry in tr_data],
        'Opening_Rank': [entry.Opening_Rank for entry in tr_data],
        'Closing_Rank': [entry.Closing_Rank for entry in tr_data]
    }
    df = pd.DataFrame(data)
    
    # Melt the DataFrame to long format
    df_melted = df.melt(id_vars='Year', value_vars=['Opening_Rank', 'Closing_Rank'], 
                        var_name='Rank_Type', value_name='Rank')

    # Create the plot
    fig = px.line(df_melted, x='Year', y='Rank', color='Rank_Type',
                  labels={'Rank': 'Rank', 'Year': 'Year', 'Rank_Type': 'Rank Type'},
                  title='Opening and Closing Ranks Over the Years')

    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Rank',
        yaxis=dict(autorange=True)
    )

    # Convert the plot to HTML
    chart = fig.to_html()

    context = {
        'chart': chart,
        'tr_data': tr_data
    }

    return render(request, 'trendsoveryears.html', context)



def trendsOverRounds(request):

    Academic_Program_Name = request.GET.get('Academic_Program_Name')
    Institute = request.GET.get('Institute')
    Seat_Type = request.GET.get('Seat_Type')
    Gender = request.GET.get('Gender')
    year = request.GET.get('year')
    
    round_data = josaa.objects.filter(
        Academic_Program_Name=Academic_Program_Name,
        Institute=Institute,
        Seat_Type=Seat_Type,
        Gender=Gender,
        year=year,
    )

    # Convert queryset to a DataFrame
    data = {
        'Round': [entry.round for entry in round_data],
        'Opening_Rank': [entry.Opening_Rank for entry in round_data],
        'Closing_Rank': [entry.Closing_Rank for entry in round_data]
    }
    df = pd.DataFrame(data)
    
    # Melt the DataFrame to long format
    df_melted = df.melt(id_vars='Round', value_vars=['Opening_Rank', 'Closing_Rank'], 
                        var_name='Rank_Type', value_name='Rank')

    # Create the plot
    fig = px.line(df_melted, x='Round', y='Rank', color='Rank_Type',
                  labels={'Rank': 'Rank', 'Round': 'Round', 'Rank_Type': 'Rank Type'},
                  title='Opening and Closing Ranks Over the Rounds')
    
    fig.update_layout(
        xaxis_title='Round',
        yaxis_title='Rank',
        yaxis=dict(autorange=True)
    )

    # Convert the plot to HTML
    chart = fig.to_html()

    context = {
        'chart': chart,
        'round_data': round_data
    }

    return render(request, 'trendsOverRounds.html', context)


def rank_input(request):
    rank_data=[]
    if request.method =='POST':
       rank = request.POST.get('rank', None)
       Seat_Type = request.POST.get('Seat_Type')
       Gender = request.POST.get('Gender')
       year = request.POST.get('year')
       round=request.POST.get('round')
   
       rank_data = josaa.objects.filter(Opening_Rank__lte=rank,
                                      Closing_Rank__gte=rank,
                                      Seat_Type=Seat_Type,
                                      Gender=Gender,
                                      year=year,
                                      round=round,)

    context = {
        'rank_data': rank_data
       }

    return render(request, 'rank_input.html', context)



def top10Trends(request):

    Academic_Program_Name = request.GET.get('Academic_Program_Name')
    Seat_Type =request.GET.get('Seat_Type')
    Gender = request.GET.get('Gender')
    year = request.GET.get('year')
    round = request.GET.get('round')
    
    institutes = [
        "Indian Institute of Technology Madras",
        "Indian Institute of Technology Delhi",
        "Indian Institute of Technology Bombay",
        "Indian Institute of Technology Kanpur",
        "Indian Institute of Technology Kharagpur",
        "Indian Institute of Technology Roorkee",
        "Indian Institute of Technology Guwahati",
        "Indian Institute of Technology Hyderabad",
        "Indian Institute of Technology Indore",
        "Indian Institute of Technology (BHU) Varanasi",
    ]

    # Create a Q object for the institutes
    institute_filter = Q()
    for institute in institutes:
        institute_filter |= Q(Institute=institute)


    top10_data = josaa.objects.filter(
        institute_filter,
        Academic_Program_Name=Academic_Program_Name,
        Seat_Type=Seat_Type,
        Gender=Gender,
        year=year,
        round=round,
        )
      # Convert queryset to a DataFrame
    data = {
        'Institute': [entry.Institute for entry in top10_data],
        'Opening_Rank': [entry.Opening_Rank for entry in top10_data],
        'Closing_Rank': [entry.Closing_Rank for entry in top10_data]
    }
    df = pd.DataFrame(data)
    
    # Melt the DataFrame to long format
    df_melted = df.melt(id_vars='Institute', value_vars=['Opening_Rank', 'Closing_Rank'], 
                        var_name='Rank_Type', value_name='Rank')

    # Create the plot
    fig = px.line(df_melted, x='Institute', y='Rank', color='Rank_Type',
                  labels={'Rank': 'Rank', 'Institute': 'Institute', 'Rank_Type': 'Rank Type'},
                  title='Trends of Opening and Closing Ranks of top 10 institutes')

    
    fig.update_layout(
        xaxis_title='Institute',
        yaxis_title='Rank',
        yaxis=dict(autorange=True)
    )

    # Convert the plot to HTML
    chart = fig.to_html()

    context = {
        'chart': chart,
        'top10_data': top10_data
    }
    
    return render(request, 'top10Trends.html', context)