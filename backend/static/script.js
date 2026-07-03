let chart = null;


function loadData() {

    fetch("/sensor-data")
    .then(response => response.json())
    .then(data => {

        displayPatients(data);

        loadD3Chart();

    });

}



function displayPatients(data){


    document.getElementById("total").textContent = data.length;


    if(data.length > 0){

        const latest = data[data.length - 1];

        document.getElementById("latestPatient").textContent = latest.patient_id;

        document.getElementById("latestStatus").textContent = latest.status;

    }


    const card = document.getElementById("patientArea");


    card.innerHTML = `

        <h2>Patient Readings</h2>

        <div id="patientList"></div>

        <hr>

        <h2>Temperature History (Chart.js)</h2>

        <canvas id="temperatureChart"></canvas>

    `;



    const patientList = document.getElementById("patientList");


    const labels = [];

    const temperatures = [];



    data.forEach(patient => {


        labels.push(patient.patient_id);

        temperatures.push(patient.temperature);



        let badge = "";


        if(patient.status.toLowerCase() === "stable"){

            badge = "<span class='stable'>Stable</span>";

        }

        else if(patient.status.toLowerCase() === "warning"){

            badge = "<span class='warning'>Warning</span>";

        }

        else{

            badge = "<span class='critical'>Critical</span>";

        }



        patientList.innerHTML += `

            <hr>


            <p><strong>Patient ID:</strong> ${patient.patient_id}</p>

            <p><strong>Name:</strong> ${patient.patient_name}</p>

            <p><strong>Age:</strong> ${patient.age}</p>

            <p><strong>Wound Location:</strong> ${patient.wound_location}</p>

            <p><strong>Temperature:</strong> ${patient.temperature} °C</p>

            <p><strong>Moisture:</strong> ${patient.moisture}%</p>

            <p><strong>Status:</strong> ${badge}</p>

            <p><strong>Recorded:</strong> ${patient.created_at}</p>


            <button 
            class="deleteButton"
            onclick="deletePatient(${patient.id})">

            Delete Record

            </button>

        `;

    });



    const ctx = document.getElementById("temperatureChart");


    if(chart){

        chart.destroy();

    }



    chart = new Chart(ctx, {

        type:"line",

        data:{

            labels:labels,

            datasets:[{

                label:"Temperature (°C)",

                data:temperatures,

                borderWidth:2,

                fill:false

            }]

        },

        options:{

            responsive:true

        }

    });


}




function searchPatient(){


    const searchValue = document
    .getElementById("searchInput")
    .value
    .toLowerCase();


    fetch("/sensor-data")
    .then(response => response.json())
    .then(data => {


        const filtered = data.filter(patient =>

            patient.patient_id
            .toLowerCase()
            .includes(searchValue)

        );


        displayPatients(filtered);

        loadD3Chart();


    });


}




function deletePatient(id){


    if(confirm("Delete this patient record?")){


        fetch("/delete/" + id, {

            method:"DELETE"

        })

        .then(response => response.json())

        .then(data => {


            alert(data.message);


            loadData();


        });


    }


}



// =================================
// D3.js Interactive Visualization
// =================================


function loadD3Chart(){


    fetch("/sensor-data")
    .then(response => response.json())
    .then(data => {


        d3.select("#d3Chart").html("");



        const width = 600;

        const height = 300;



        const svg = d3.select("#d3Chart")

        .append("svg")

        .attr("width", width)

        .attr("height", height);



        const xScale = d3.scaleBand()

        .domain(data.map(patient => patient.patient_id))

        .range([50, width - 30])

        .padding(0.3);



        const yScale = d3.scaleLinear()

        .domain([0,45])

        .range([height - 40,20]);



        svg.selectAll("rect")

        .data(data)

        .enter()

        .append("rect")

        .attr("x", patient => xScale(patient.patient_id))

        .attr("y", patient => yScale(patient.temperature))

        .attr("width", xScale.bandwidth())

        .attr(
            "height",

            patient => height - 40 - yScale(patient.temperature)

        );



        svg.selectAll("text")

        .data(data)

        .enter()

        .append("text")

        .text(patient => patient.temperature + "°C")

        .attr("x", patient => xScale(patient.patient_id))

        .attr("y", patient => yScale(patient.temperature) - 5);


    });


}




loadData();


setInterval(loadData,5000);