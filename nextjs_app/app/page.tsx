"use client";

import { useState } from "react";

export default function Home() {
  const [companies, setCompanies] = useState([]);
  const [positions, setPositions] = useState([]);

  return (
    <div className="bg-white min-h-screen text-black">
      <div className="flex">
        {/* LEFT COLUMN */}
        <div className="w-1/2 p-4">
          <InputSection 
            title="Companies"
            placeholder="Add a company"
            data={companies}
            setData={setCompanies}
          />
          <InputSection 
            title="Companies"
            placeholder="Add a company"
            data={positions}
            setData={setPositions}
          />
        </div>
        {/* RIGHT COLUMN */}
        <div></div>
      </div>
    </div>
  );
}
