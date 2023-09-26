import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from './components/common/Layout';
import CreatePage from './components/CreatePage';
import ListPage from './components/ListPage';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<CreatePage />} />
          <Route path="list" element={<ListPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(<App />);