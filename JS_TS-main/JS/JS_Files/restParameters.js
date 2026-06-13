//rest parameter: ...

function selectCountryFromDrpdwn(countryName){
    console.log('Select country: ', countryName);
}

selectCountryFromDrpdwn('India');//Select country:  India
//Consider the dropdown is multi-select dropdown. What if I want to select multiple countries at the same time.
selectCountryFromDrpdwn('India', 'UAE', 'UK', 'USSR');//Select country:  India

//To address above problem, we can use rest parameter --> ...

function selectCountryFromDrpdwn1(...countryName){
    console.log('Select country: ', countryName);
    console.log(countryName.length);
}
selectCountryFromDrpdwn1('India', 'UAE', 'UK', 'USSR');
/*
Select country:  [ 'India', 'UAE', 'UK', 'USSR' ]
4
*/

function selectCountryFromDrpdwn2(...countryName){
    console.log('Select country: ', countryName);
    console.log(countryName.length);

    for(let e of countryName){
        console.log(e);
    };
}
selectCountryFromDrpdwn2('India', 'UAE', 'UK', 'USSR', 'France');
/*
Select country:  [ 'India', 'UAE', 'UK', 'USSR', 'France' ]
5
India
UAE
UK
USSR
France
*/

//Example:
function fillValues(name, ...details){
    console.log(`Checking details for ${name}: `, details);
    console.log(details.length);

    for(let val of details){
        console.log(val);
    }
}
fillValues('Sachin', 101, 'New Colony', 'Sector7', 'Bangalore', 110231, 'India');
/*
Checking details for Sachin:  [ 101, 'New Colony', 'Sector7', 'Bangalore', 110231, 'India' ]
6
101
New Colony
Sector7
Bangalore
110231
India
*/