import React, { useState } from 'react';
import './App.css';

function HomeScreen({ onAddName, onShowDistances, onCompetitionMode }) {
  return (
    <div>
      <h1>Home Screen</h1>
      <button onClick={onAddName}>Add Name</button>
      <button onClick={onShowDistances}>Show Distances</button>
      <button onClick={onCompetitionMode}>Competition Mode</button>
    </div>
  );
}

function AddNameScreen({ onSaveName, onDeleteName, onHome }) {
  const [name, setName] = useState('');

  const handleSaveName = () => {
    onSaveName(name);
    setName('');
  };

  return (
    <div>
      <h1>Add Name Screen</h1>
      <input
        type="text"
        placeholder="Enter name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <button onClick={handleSaveName}>Save Name</button>
      <button onClick={onDeleteName}>Delete Name</button>
      <button onClick={onHome}>Home</button>
    </div>
  );
}

function DistancesScreen({ onAddDistance, onRemoveDistance, onHome, names, distances }) {
  const [name, setName] = useState('');
  const [distance, setDistance] = useState('');

  const handleAddDistance = () => {
    onAddDistance(name, parseFloat(distance));
    setName('');
    setDistance('');
  };

  return (
    <div>
      <h1>Distances Screen</h1>
      <input
        type="text"
        placeholder="Enter name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        type="text"
        placeholder="Enter distance"
        value={distance}
        onChange={(e) => setDistance(e.target.value)}
      />
      <button onClick={handleAddDistance}>Add Distance</button>
      <button onClick={() => onRemoveDistance(name)}>Remove Distance</button>
      <button onClick={onHome}>Home</button>

      <div>
        <h2>Distances</h2>
        <ul>
          {names.map((n, index) => (
            <li key={n}>
              {n}: {distances[index]}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

function CompetitionScreen({ onHome, names, distances }) {
  const sortedData = names
    .map((name, index) => ({ name, distance: distances[index] }))
    .sort((a, b) => a.distance - b.distance);

  return (
    <div>
      <h1>Competition Screen</h1>
      <button onClick={onHome}>Home</button>

      <div>
        <h2>Competition Standings</h2>
        <ul>
          {sortedData.map(({ name, distance }) => (
            <li key={name}>
              {name}: {distance}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

function App() {
  const [currentScreen, setCurrentScreen] = useState('home');
  const [names, setNames] = useState([]);
  const [distances, setDistances] = useState([]);

  const navigateTo = (screen) => setCurrentScreen(screen);

  const handleAddName = (name) => setNames([...names, name]);
  const handleDeleteName = (name) => setNames(names.filter((n) => n !== name));

  const handleAddDistance = (name, distance) => {
    const index = names.indexOf(name);
    if (index !== -1) {
      const newDistances = [...distances];
      newDistances[index] = distance;
      setDistances(newDistances);
    } else {
      setNames([...names, name]);
      setDistances([...distances, distance]);
    }
  };

  const handleRemoveDistance = (name) => {
    const index = names.indexOf(name);
    if (index !== -1) {
      const newNames = [...names];
      const newDistances = [...distances];
      newNames.splice(index, 1);
      newDistances.splice(index, 1);
      setNames(newNames);
      setDistances(newDistances);
    }
  };

  const screens = {
    home: (
      <HomeScreen
        onAddName={() => navigateTo('addName')}
        onShowDistances={() => navigateTo('distances')}
        onCompetitionMode={() => navigateTo('competition')}
      />
    ),
    addName: (
      <AddNameScreen
        onSaveName={handleAddName}
        onDeleteName={() => navigateTo('home')}
        onHome={() => navigateTo('home')}
      />
    ),
    distances: (
      <DistancesScreen
        onAddDistance={handleAddDistance}
        onRemoveDistance={handleRemoveDistance}
        onHome={() => navigateTo('home')}
        names={names}
        distances={distances}
      />
    ),
    competition: (
      <CompetitionScreen onHome={() => navigateTo('home')} names={names} distances={distances} />
    ),
  };

  return <div className="App">{screens[currentScreen]}</div>;
}

export default App;
