import logo from './logo.svg';
import './App.css';
import Greeting from './components/pure/greeting';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {/*Componente propio Greeting. Creo una nueva instancia del componente*/}
        <Greeting name="Joel"></Greeting>
        </header>
    </div>
  );
}

export default App;
