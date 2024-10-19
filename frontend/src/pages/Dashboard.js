import React, { useState } from 'react';

export default function Dashboard() {
  const [foodName, setFoodName] = useState('');         // For storing the food name
  const [weightInGrams, setWeightInGrams] = useState(0); // For storing the quantity in grams
  const [nutrientInfo, setNutrientInfo] = useState(); // For storing nutrient information
  const [disabledFlag, setDisabledFlag] = useState(false);
  const [buttonText, setButtonText] = useState('Submit');

  const handleSubmit = async (e) => {

    e.preventDefault();

    if (foodName === '') {
      alert("Food name can't be empty");
      return;
    }

    // Disabling submit button to avoid multiple requests
    setDisabledFlag(true);
    setButtonText('Loading...');
    
    // Fetch data from the backend API
    const response = await fetch(`http://localhost:8000/food/${foodName}/${weightInGrams}`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    });

    if (response.status === 200) {
      const result = await response.json();
      if (result.Error) {
        alert(result.Error);
        setDisabledFlag(false);
        setButtonText('Submit');
      }
      else{
        setNutrientInfo(result);
        setDisabledFlag(false);
        setButtonText('Submit');
      }
    }

    if(response.status != 200){
      alert(response.statusText);
    }
  };

  return (
    <>
      <body>
        <div className='page-wrapper'>
          <div className='page-body'>
            <div className='page page-center'>
              <div className='container container-tight py-5'>
                <div className='row'>
                    <div className='card card-md'>
                      <div className='card-body'>
                        <h2 className='text-center mb-4'>Enter Food & Quantity</h2>
                        <div className='mb-3'>
                          <label className='form-label required'>Food Item</label>
                          <input
                            className='form-control'
                            type='text'
                            value={foodName}
                            onChange={(e) => setFoodName(e.target.value)}
                          />
                        </div>
                        <div className='mb-3'>
                          <label className='form-label required'>Quantity in grams</label>
                          <input
                            className='form-control'
                            type='number'
                            value={weightInGrams}
                            onChange={(e) => setWeightInGrams(e.target.value)}
                          />
                        </div>
                        <button 
                          className='btn btn-green' 
                          name="submit" 
                          onClick={handleSubmit}
                          disabled={disabledFlag}>{buttonText}</button>
                      </div>
                    </div>
                    <div className='card'>
                      <div className="list-group list-group-flush overflow-auto" style={{ maxHeight: '55vh' }}>
                        {/* Remove dummy text and display nutrient information */}
                        {nutrientInfo ? (
                          <>
                            <div className='list-group-item'>Calories: {nutrientInfo.Calories}</div>
                            <div className='list-group-item'>Protein: {nutrientInfo.Protein}</div>
                            <div className='list-group-item'>Fat: {nutrientInfo.Fat}</div>
                            <div className='list-group-item'>Carbohydrates: {nutrientInfo.Carbohydrates}</div>
                            <div className='list-group-item'>Fiber: {nutrientInfo.Fiber}</div>
                            <div className='list-group-item'>Sugars: {nutrientInfo.Sugars}</div>
                            <div className='list-group-item'>
                              <h4>Vitamins and Minerals:</h4>
                              {nutrientInfo['Vitamins and Minerals'] && Object.keys(nutrientInfo['Vitamins and Minerals']).length > 0 ? (
                                Object.entries(nutrientInfo['Vitamins and Minerals']).map(([key, value]) => (
                                  <div key={key} className='list-group-item'>
                                    {key}: {value}
                                  </div>
                                ))
                              ) : (
                                <div className='list-group-item'>No vitamins and minerals data available.</div>
                              )}
                            </div>
                          </>
                        ) : (
                          <div className='list-group-item'>Enter food and quantity to see nutrient information</div>
                        )}
                      </div>
                    </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </body>
    </>
  );
}