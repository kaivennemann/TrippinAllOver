import logo from './logo.svg';
import './output.css';

function App() {
  return (
    <div class="grid md:grid-cols-2 py-8 md:px-16">
        <div class="md:mb-0 md:mr-8">
            <div class="mb-10 md:mb-14">
                <p class="text-center text-navy-blue text-4xl lg:text-8xl font-bold">Find your next</p>
                <p class="text-center text-navy-blue text-6xl lg:text-9xl font-bold">WEEKEND GETAWAY!</p>
            </div>
            <div class="p-4 md:p-0">
                <div class="rounded-large w-full p-4 bg-white sm:p-6 md:p-8">
                    <div class="space-y-6">
                        <h5 class="text-xl font-medium text-gray-900">Your ideal holiday...on a budget!</h5>
                        <div>
                            <label for="outbound" class="block mb-2 text-sm font-medium text-light-black">Outbound Airport</label>
                            <select name="outbound" id="outbound" class="bg-light-gray border border-gray text-light-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
                                    <option value="STN">London Stansted (STN)</option>
                            </select>
                        </div>
                        <div class="grid md:grid-cols-2">
                            <div class="md:mr-2">
                                <label for="start-date" class="block mb-2 text-sm font-medium text-light-black">Select times of travel:</label>
                                <input type="date" id="start-date" name="start-date" value="2023-10-01" min="2023-01-01" max="2025-12-31" class="bg-light-gray border border-gray text-light-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"/>
                            </div>
                            <div class="md:ml-2">
                                <label for="end-date" class="block mb-2 text-sm font-medium text-light-black">until:</label>
                                <input type="date" id="end-date" name="end-date" value="2023-10-03" min="2023-08-23" max="2025-12-31" class="bg-light-gray border border-gray text-light-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"/>
                            </div>
                        </div>
                        <button type="button" onclick="single_trip()" class="w-full bg-purple hover:bg-blue active:text-white font-medium rounded text-sm px-5 py-2.5 text-center">Find Trips</button>
                    </div>
                </div>
            </div>

            <div class="p-4 md:p-0">
                <div class="rounded-large w-full p-4 bg-white sm:p-6 md:p-8">
                    <div class="space-y-6">
                        <div>
                            <label for="outbound" class="block mb-2 text-sm font-medium text-light-black">Outbound Airport</label>
                            <select name="outbound" id="outbound" class="bg-light-gray border border-gray text-light-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
                                    <option value="STN">London Stansted (STN)</option>
                            </select>
                        </div>

                        <div class="grid grid-cols-1">
                            <div class="flex flex-row">

                                <div class="p-2">
                                    <button type="button" onclick="calendar_left()" class="bg-light-gray border border-gray text-light-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5"></button>
                                </div>

                                <div class="p-2">
                                    <label for="month-select" class="sr-only">Select Month</label>
                                    <select id="month-select" class="bg-light-gray border border-gray text-light-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5">
                                        <option value="1">January</option>
                                        <option value="2">February</option>
                                        <option value="3">March</option>
                                        <option value="4">April</option>
                                        <option value="5">May</option>
                                        <option value="6">June</option>
                                        <option value="7">July</option>
                                        <option value="8">August</option>
                                        <option value="9">September</option>
                                        <option value="10">October</option>
                                        <option value="11">November</option>
                                        <option value="12">December</option>
                                    </select>
                                </div>

                                <div class="p-2">
                                    <label for="year-select" class="sr-only">Select Year</label>
                                    <select id="year-select" class="bg-light-gray border border-gray text-light-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5">
                                        TODO: make this dynamically generated
                                        <option value="2023">2023</option>
                                        <option value="2024">2024</option>
                                        <option value="2025">2025</option>
                                        <option value="2026">2026</option>
                                        <option value="2027">2027</option>

                                    </select>
                                </div>
                                <div class="p-2">
                                     <button  type="button" onclick="calendar_right()" class="bg-light-gray border border-gray text-light-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5"></button>
                                </div>

                            </div>

                            <div id="calendar-body"></div>
                        </div>


                        <button type="button" onclick="send_calendar_data()" class="w-full bg-sky-800 hover:bg-blue active:text-white font-medium rounded text-sm px-5 py-2.5 text-center">Find Trips</button>
                    </div>
                </div>
            </div>

            <div class="p-4 md:p-0">
                <div class="rounded-large w-full p-4 bg-white sm:p-6 md:p-8">
                    <div id="results-container" class="space-y-6">
                        Results will be displayed here
                    </div>
                </div>
            </div>

        </div>
    </div>
  );
}

export default App;
