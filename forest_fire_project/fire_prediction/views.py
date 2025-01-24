from django.shortcuts import render
from .forms import FirePredictionForm
from .utils import load_model

# Load the model once during initialization
model = load_model()

def predict_fire(request):
    prediction = None
    if request.method == 'POST':
        form = FirePredictionForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            data = form.cleaned_data
            # Prepare input for the model
            model_input = [[
                data['latitude'],
                data['longitude'],
                data['brightness'],
                data['satellite'],
                data['frp'],
                data['daynight'],
                int(data['type_2']),
                int(data['type_3']),
                data['scan_binned'],
                data['year'],
                data['month'],
                data['day']
            ]]
            # Make prediction
            prediction = model.predict(model_input)[0]
    else:
        form = FirePredictionForm()
    
    return render(request, 'fire_prediction/predict.html', {'form': form, 'prediction': prediction})
